#!/usr/bin/env python3
"""Sync released Obsidian notes into the Jekyll site.

Reads only the folders listed in tools/sync.yml (allowlist-only), rewrites the
website copy of each note (frontmatter normalized, Obsidian syntax converted),
copies referenced images and reports anything it could not resolve.

Vault files are never modified.

Usage:
    python3 tools/sync.py [--dry-run]
"""

from __future__ import annotations

import datetime as dt
import fnmatch
import html
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path(__file__).resolve().parent / "sync.yml"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}

RE_EMBED = re.compile(r"!\[\[([^\]|#]+?)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]")
RE_WIKILINK_HEAD = re.compile(r"\[\[#([^\]|]+?)(?:\|([^\]]*))?\]\]")
RE_WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+?)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]")
RE_HIGHLIGHT = re.compile(r"==([^=\n]+)==")
RE_FENCE = re.compile(r"^(```|~~~)")
RE_INLINE_CODE = re.compile(r"(`[^`]*`)")
RE_CALLOUT = re.compile(r"^>\s*\[!([a-zA-Z-]+)\]([+-]?)\s*(.*)$")
RE_HEAD = re.compile(r"^(#{1,6})\s")
RE_FN_DEF = re.compile(r"^\[\^([^\]]+)\]:\s?(.*)$")
RE_FN_REF = re.compile(r"\[\^([^\]]+)\]")
RE_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


# ---------------------------------------------------------------- utilities

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def load_config() -> dict:
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))

    def expand(s: str) -> str:
        for k, v in cfg.get("vault_roots", {}).items():
            s = s.replace("{" + k + "}", v)
        return s

    for src in cfg["sources"]:
        src["root"] = Path(expand(src["root"]))
        src["out_dir"] = ROOT / src["out_dir"]
        src["derive_tags"] = cfg.get("derive_tags", {}).get(src["name"], [])
    cfg["image_search_roots"] = [Path(expand(p)) for p in cfg["image_search_roots"]]
    return cfg


def normalize_date(value, fallback: dt.datetime) -> str:
    if isinstance(value, dt.datetime):
        return value.isoformat(timespec="minutes")
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, str) and value.strip():
        return value.strip()
    # mtime fallback: keep the local UTC offset so CI (UTC) can't read it
    # as a future date
    return fallback.astimezone().isoformat(timespec="minutes")


def split_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            raw = text[4:end]
            body = text[end + 5:]
            try:
                fm = yaml.safe_load(raw) or {}
                if isinstance(fm, dict):
                    return fm, body
            except yaml.YAMLError:
                pass
    return {}, text


def excluded(rel: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, g) for g in globs)


# ------------------------------------------------------------------- images

class ImageIndex:
    def __init__(self, roots: list[Path]):
        self.by_name: dict[str, list[Path]] = {}
        for root in roots:
            if not root.is_dir():
                continue
            for p in root.rglob("*"):
                if p.is_file() and p.suffix.lower() in IMAGE_EXTS:
                    self.by_name.setdefault(p.name.lower(), []).append(p)

    def resolve(self, ref: str, note: "Note") -> Path | None:
        ref = ref.strip()
        cands = self.by_name.get(posix_basename(ref).lower(), [])
        if not cands:
            return None
        same_dir = [c for c in cands if note.path.parent in c.parents]
        if same_dir:
            return same_dir[0]
        if "/" in ref:
            exact = [c for c in cands if c.as_posix().endswith(ref)]
            if exact:
                return exact[0]
        return cands[0]


def posix_basename(ref: str) -> str:
    return ref.replace("\\", "/").rsplit("/", 1)[-1]


# -------------------------------------------------------------------- notes

class Note:
    def __init__(self, src: dict, path: Path):
        self.src = src
        self.path = path
        self.rel = path.relative_to(src["root"])
        self.parts = self.rel.with_suffix("").parts
        self.slugs = [slugify(p) for p in self.parts]
        self.platform = src["platform"]

        self.fm, body = split_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        self.body = RE_CONTROL.sub("", body)
        self.warnings: list[str] = []
        self.images: dict[str, str] = {}           # copied images for this note
        self.rendered: str | None = None            # memoized standalone body
        self.rendered_embed: str | None = None      # memoized transcluded body

        self.title = str(self.fm.get("title") or self.parts[-1]).strip()
        desc = self.fm.get("description") or self.fm.get("Description") or ""
        self.description = str(desc).strip()
        self.date = normalize_date(self.fm.get("date"), dt.datetime.fromtimestamp(path.stat().st_mtime))

        # ---- classification --------------------------------------------
        self.layout = src["layout"]
        self.kind = "note"

        if self.platform == "ctf":
            # event overview candidate: named like its folder (BKCTF/BKCTF.md,
            # 0xFUN/0xFUN CTF.md). The winner is elected after collection.
            self.overview_candidate = (
                len(self.slugs) >= 2
                and (self.slugs[-1] == self.slugs[-2]
                     or self.slugs[-1] in (self.slugs[-2] + "-ctf", self.slugs[-2] + "-writeups"))
            )
        else:
            self.overview_candidate = False

        if self.platform == "privacy":
            if len(self.parts) == 1:
                self.kind = "privacy-hub"
                self.layout = "privacy-hub"
                if self.rel.as_posix() == src.get("overview_note"):
                    self.kind = "privacy-overview"
                self.category = self.title
            else:
                self.layout = "privacy-doc"
                self.category = self.parts[0]

        # folder-derived metadata
        self.year = self.parts[0] if self.platform == "ctf" and len(self.parts) >= 2 else None
        self.event = self.parts[-2] if self.platform == "ctf" and len(self.parts) >= 2 else None
        self.season = None
        if self.platform == "htb" and len(self.parts) >= 2:
            m = re.search(r"(\d+)", self.parts[0])
            self.season = m.group(1) if m else self.parts[0]

        self.url = src["url_prefix"] + "/" + "/".join(self.slugs) + "/"

    @property
    def priority(self) -> int:
        try:
            return int(self.fm.get("priority", 99))
        except (TypeError, ValueError):
            return 99

    def meta(self, prev_url: str | None, next_url: str | None) -> dict:
        m: dict = {
            "layout": self.layout,
            "title": self.title,
            "description": self.description,
            # explicit excerpt avoids Jekyll auto-splitting the {% raw %} body
            "excerpt": self.description,
            "date": self.date,
            "platform": self.platform,
            "permalink": self.url,
        }
        if self.platform == "htb":
            m["os"] = str(self.fm.get("os", "")).strip()
            m["difficulty"] = str(self.fm.get("difficulty", "")).strip()
            m["season"] = self.season
        elif self.platform == "ctf":
            if self.year:
                m["year"] = str(self.year)
            if self.event:
                m["event"] = self.event
        elif self.platform == "privacy":
            m["category"] = self.category

        # derived tags (site tags come from metadata, not vault frontmatter)
        tags = list(self.src.get("derive_tags", []))
        if self.platform == "htb":
            for v in (self.fm.get("os"), self.fm.get("difficulty")):
                if v and str(v).strip() and str(v).strip().lower() not in [t.lower() for t in tags]:
                    tags.append(str(v).strip().lower())
        elif self.platform == "ctf":
            if self.year and str(self.year) not in tags:
                tags.append(str(self.year))
        elif self.platform == "privacy":
            if self.category and self.category not in tags:
                tags.append(self.category)
        m["tags"] = tags

        if prev_url:
            m["prev_url"] = prev_url
        if next_url:
            m["next_url"] = next_url
        return m


# --------------------------------------------------------------- transforms

class Context:
    """Shared state for rendering: image index, note index, unresolved refs."""

    def __init__(self, img_index: ImageIndex):
        self.img_index = img_index
        self.notes_by_key: dict[str, Note] = {}
        self.unresolved: list[str] = []


def index_note(ctx: Context, note: Note) -> None:
    for key in [note.title, note.parts[-1], *(note.fm.get("aliases") or [])]:
        ctx.notes_by_key.setdefault(str(key).strip().lower(), note)


def render_note(note: Note, ctx: Context, stack: tuple = (), embed: bool = False) -> str:
    cached = note.rendered_embed if embed else note.rendered
    if cached is not None:
        return cached
    if note in stack:  # embed cycle guard
        return ""
    return transform_body(note, ctx, stack + (note,), embed)


def transform_body(note: Note, ctx: Context, stack: tuple = (), embed: bool = False) -> str:
    out_lines: list[str] = []
    lines = note.body.splitlines()

    # Footnote scoping for embeds: kramdown renders footnotes at the bottom of
    # the whole page, but a transcluded note must keep its footnotes inside its
    # own card. Extract the definitions, number the references, and append a
    # scoped footnote list at the end of the embed body.
    fn_key = "-".join(note.slugs)
    fn_defs: dict[str, str] = {}
    fn_nums: dict[str, int] = {}
    if embed:
        kept: list[str] = []
        j = 0
        fenced = False
        while j < len(lines):
            if RE_FENCE.match(lines[j]):
                fenced = not fenced
                kept.append(lines[j])
                j += 1
                continue
            m = RE_FN_DEF.match(lines[j]) if not fenced else None
            if m:
                fid, text = m.group(1), m.group(2)
                j += 1
                while j < len(lines) and lines[j][:1] in (" ", "\t") and lines[j].strip():
                    text += " " + lines[j].strip()
                    j += 1
                fn_defs[fid] = text
                continue
            kept.append(lines[j])
            j += 1
        lines = kept

    i = 0
    in_fence = False

    def handle_embed(line: str) -> str:
        def rep(m: re.Match) -> str:
            ref, _anchor, size = m.group(1).strip(), m.group(2), m.group(3)
            name = posix_basename(ref)

            # excalidraw drawing: try an exported image first
            if name.lower().endswith(".excalidraw"):
                export = ctx.img_index.resolve(name.rsplit(".", 1)[0] + ".png", note)
                if export:
                    ref = name = export.name
                else:
                    ctx.unresolved.append(f"{note.rel}: dropped drawing embed '![[{ref}]]'")
                    return ""

            img = ctx.img_index.resolve(ref, note)
            if img is not None:
                if img.name not in note.images:
                    slug = "-".join(note.slugs)
                    dest = ROOT / "assets" / "content" / note.platform / slug / img.name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    if not dest.exists():
                        shutil.copy2(img, dest)
                    site_url = "/assets/content/" + "/".join(dest.relative_to(ROOT / "assets" / "content").parts)
                    note.images[img.name] = quote(site_url, safe="/")
                attrs = ""
                if size:
                    size = size.strip()
                    if re.fullmatch(r"\d+", size):
                        attrs += f' width="{size}"'
                    elif re.fullmatch(r"\d+x\d+", size):
                        w, h = size.split("x")
                        attrs += f' width="{w}" height="{h}"'
                alt = img.stem if not img.stem.lower().startswith("pasted image") else note.title
                alt = html.escape(RE_CONTROL.sub("", alt), quote=True)
                return (f'<img class="content-image" src="{note.images[img.name]}"'
                        f' alt="{alt}" loading="lazy"{attrs}>')

            # note embed: transclude the target note as a document card
            key = re.sub(r"\.(md|markdown)$", "", ref, flags=re.I).strip().lower()
            target = ctx.notes_by_key.get(key)
            if target is not None and target is not note:
                body = render_note(target, ctx, stack, embed=True)
                title = html.escape(target.title, quote=True)
                return (
                    f'<div class="note-embed">\n\n'
                    f'<div class="note-embed-head"><a class="note-embed-title" href="{target.url}">{title}</a>'
                    f'<span class="note-embed-meta">Updated {target.date[:10]}</span>\n'
                    f'</div>\n\n'
                    f'<div class="note-embed-body">\n\n{body}\n\n</div>\n\n'
                    f'<div class="note-embed-foot">'
                    f'<a href="{target.url}">Open the full note →</a>\n'
                    f'</div>\n\n'
                    f'</div>'
                )

            ctx.unresolved.append(f"{note.rel}: missing embed '![[{ref}]]'")
            return ""

        return RE_EMBED.sub(rep, line)

    def handle_links(line: str) -> str:
        def rep_head(m: re.Match) -> str:
            anchor, alias = m.group(1).strip(), m.group(2)
            text = (alias or anchor).strip()
            return f'<a class="obsidian-link" href="#{slugify(anchor)}">{text}</a>'

        def rep(m: re.Match) -> str:
            target, anchor, alias = m.group(1).strip(), m.group(2), m.group(3)
            key = re.sub(r"\.(md|markdown)$", "", target, flags=re.I).strip().lower()
            hit = ctx.notes_by_key.get(key)
            text = (alias or target).strip()
            if hit is None:
                ctx.unresolved.append(f"{note.rel}: link to unpublished note '[[{target}]]' shown as text")
                return f'<span class="obsidian-link-missing" title="Not published">{text}</span>'
            url = hit.url + ("#" + slugify(anchor) if anchor else "")
            return f'<a class="obsidian-link" href="{url}">{text}</a>'

        line = RE_WIKILINK_HEAD.sub(rep_head, line)
        return RE_WIKILINK.sub(rep, line)

    def handle_fn_refs(line: str) -> str:
        def rep(m: re.Match) -> str:
            fid = m.group(1)
            if fid not in fn_defs:
                return m.group(0)          # no definition: leave untouched
            if fid not in fn_nums:
                fn_nums[fid] = len(fn_nums) + 1
                return (f'<sup class="fn-ref" id="fnref-{fn_key}-{fid}">'
                        f'<a href="#fn-{fn_key}-{fid}">{fn_nums[fid]}</a></sup>')
            return (f'<sup class="fn-ref">'
                    f'<a href="#fn-{fn_key}-{fid}">{fn_nums[fid]}</a></sup>')
        return RE_FN_REF.sub(rep, line)

    def convert_part(part: str) -> str:
        part = handle_embed(part)
        part = handle_links(part)
        part = RE_HIGHLIGHT.sub(r"<mark>\1</mark>", part)
        if fn_defs:
            part = handle_fn_refs(part)
        return part

    while i < len(lines):
        line = lines[i]

        # fenced code blocks pass through untouched
        if RE_FENCE.match(line):
            in_fence = not in_fence
            out_lines.append(line)
            i += 1
            continue
        if in_fence:
            out_lines.append(line)
            i += 1
            continue

        # callouts: > [!type] title  + following "> " lines
        m = RE_CALLOUT.match(line)
        if m:
            ctype, fold, title = m.group(1).lower(), m.group(2), m.group(3).strip()
            block = []
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                block.append(lines[i].lstrip()[1:].lstrip())
                i += 1
            inner = "\n".join(convert_part(b) for b in block)
            fold_cls = f" callout-foldable{' open' if fold == '+' else ''}" if fold else ""
            title_html = f'<p class="callout-title">{convert_part(title)}</p>' if title else ""
            out_lines.append(
                f'<div class="callout callout-{ctype}{fold_cls}">{title_html}'
                f'<div class="callout-body">\n\n{inner}\n\n</div></div>'
            )
            out_lines.append("")
            continue

        # normal markdown line, inline code spans protected
        if embed:
            m = RE_HEAD.match(line)
            if m:
                level = min(len(m.group(1)) + 2, 6)   # demote: embeds are subsections
                line = "#" * level + line[len(m.group(1)):]
        parts = RE_INLINE_CODE.split(line)
        out_lines.append("".join(p if p.startswith("`") and p.endswith("`") and len(p) > 1
                                 else convert_part(p) for p in parts))
        i += 1

    result = "\n".join(out_lines)

    # scoped footnote list at the bottom of the embed card
    if embed and fn_nums:
        items = []
        for fid, n in sorted(fn_nums.items(), key=lambda kv: kv[1]):
            text = convert_part(fn_defs[fid])
            items.append(f'{n}. <span id="fn-{fn_key}-{fid}"></span>{text} '
                         f'<a class="fn-back" href="#fnref-{fn_key}-{fid}">↩</a>')
        result += ("\n\n<div class=\"note-embed-footnotes\">\n\n"
                   + "\n".join(items) + "\n\n</div>")

    if embed:
        note.rendered_embed = result
    else:
        note.rendered = result
    return result


# ------------------------------------------------------------- privacy nav

def write_privacy_nav(notes: list[Note], dry_run: bool) -> None:
    privacy = [n for n in notes if n.platform == "privacy"]
    if not privacy:
        return
    overview = next((n for n in privacy if n.kind == "privacy-overview"), None)
    hubs = {n.category: n for n in privacy if n.kind == "privacy-hub"}
    docs: dict[str, list[Note]] = {}
    for n in privacy:
        if n.kind == "note":
            docs.setdefault(n.category, []).append(n)

    categories = []
    for name in sorted(set(hubs) | set(docs)):
        hub = hubs.get(name)
        cat_docs = sorted(docs.get(name, []), key=lambda n: n.date, reverse=True)
        categories.append({
            "name": name,
            "url": hub.url if hub else None,
            "priority": hub.priority if hub else 99,
            "notes": [{"title": d.title, "url": d.url, "date": d.date[:10]} for d in cat_docs],
        })
    categories.sort(key=lambda c: (c["priority"], c["name"].lower()))

    recent = [n for n in privacy if n.kind == "note"] or privacy
    latest = max(recent, key=lambda n: n.date)
    data = {
        "overview": {"title": overview.title, "url": overview.url} if overview else None,
        "latest": {"title": latest.title, "url": latest.url},
        "categories": categories,
    }
    if not dry_run:
        (ROOT / "_data").mkdir(exist_ok=True)
        out = ("# GENERATED by tools/sync.py -- do not edit by hand\n"
               + yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
        (ROOT / "_data" / "privacy_nav.yml").write_text(out, encoding="utf-8")


# --------------------------------------------------------------------- main

def main() -> int:
    dry_run = "--dry-run" in sys.argv
    cfg = load_config()

    ctx = Context(ImageIndex(cfg["image_search_roots"]))

    notes: list[Note] = []
    for src in cfg["sources"]:
        root: Path = src["root"]
        if not root.is_dir():
            print(f"!! source root missing: {root}", file=sys.stderr)
            continue
        for path in sorted(root.rglob("*.md")):
            rel = path.relative_to(root).as_posix()
            if excluded(rel, cfg.get("exclude_globs", [])):
                continue
            notes.append(Note(src, path))

    # elect the event overview note per CTF event folder (shortest matching stem)
    groups: dict = {}
    for n in notes:
        if n.overview_candidate:
            groups.setdefault(n.rel.parent, []).append(n)
    for group in groups.values():
        winner = min(group, key=lambda n: len(n.slugs[-1]))
        winner.kind = "event-overview"
        winner.layout = "ctf-event"
        winner.url = winner.src["url_prefix"] + "/" + "/".join(winner.slugs[:-1]) + "/"

    for n in notes:
        index_note(ctx, n)

    # prev/next within a series (same folder), ordered by date
    series: dict[tuple, list[Note]] = {}
    for n in notes:
        if n.platform in ("htb", "ctf") and n.kind == "note":
            series.setdefault((n.platform, n.rel.parent), []).append(n)
    neighbors: dict[str, tuple] = {}
    for group in series.values():
        group.sort(key=lambda n: n.date)
        for idx, n in enumerate(group):
            neighbors[n.url] = (
                group[idx - 1].url if idx > 0 else None,
                group[idx + 1].url if idx < len(group) - 1 else None,
            )

    # write notes
    if not dry_run:
        for src in cfg["sources"]:
            if src["out_dir"].exists():
                shutil.rmtree(src["out_dir"])
        content_dir = ROOT / "assets" / "content"
        if content_dir.exists():
            shutil.rmtree(content_dir)

    counts = {src["name"]: 0 for src in cfg["sources"]}
    img_count = 0
    for n in notes:
        prev_url, next_url = neighbors.get(n.url, (None, None))
        meta = n.meta(prev_url, next_url)
        body = render_note(n, ctx)
        img_count += len(n.images)
        # {% raw %} keeps payloads like {{7*7}} in writeups from being
        # interpreted as Liquid templates
        out = ("---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)
               + "---\n\n{% raw %}\n" + body + "\n{% endraw %}\n")
        dest = n.src["out_dir"] / n.rel
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(out, encoding="utf-8")
        counts[n.src["name"]] += 1

    # stub landing pages for CTF events without an overview note
    stubs: list[str] = []
    overview_urls = {n.url for n in notes if n.kind == "event-overview"}
    ctf_src = next(s for s in cfg["sources"] if s["platform"] == "ctf")
    events: dict[tuple, list[Note]] = {}
    for n in notes:
        if n.platform == "ctf" and n.kind == "note" and n.year and n.event:
            events.setdefault((n.year, n.event), []).append(n)
    for (year, event), challenges in sorted(events.items()):
        url = f"{ctf_src['url_prefix']}/{slugify(year)}/{slugify(event)}/"
        if url in overview_urls:
            continue
        meta = {
            "layout": "ctf-event",
            "title": event,
            "description": f"{len(challenges)} challenge write-ups from {event}.",
            "platform": "ctf",
            "year": str(year),
            "event": event,
            "tags": ["CTF", str(year)],
            "permalink": url,
        }
        stub = "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n"
        dest = ctf_src["out_dir"] / str(year) / event / f"{slugify(event)}.md"
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(stub, encoding="utf-8")
        stubs.append(f"event page for {event} {year} (no overview note)")

    # stub category hubs for privacy folders without a hub note
    privacy_srcs = [s for s in cfg["sources"] if s["platform"] == "privacy"]
    if privacy_srcs:
        psrc = privacy_srcs[0]
        hub_slugs = {n.slugs[0] for n in notes if n.platform == "privacy" and len(n.slugs) == 1}
        for folder in sorted(psrc["root"].iterdir()):
            if not folder.is_dir() or folder.name.startswith((".", "_")):
                continue
            if slugify(folder.name) in hub_slugs:
                continue
            meta = {
                "layout": "privacy-hub",
                "title": folder.name,
                "description": f"Notes about {folder.name.lower()}.",
                "platform": "privacy",
                "category": folder.name,
                "tags": ["Privacy", folder.name],
                "permalink": f"{psrc['url_prefix']}/{slugify(folder.name)}/",
            }
            stub = "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n"
            dest = psrc["out_dir"] / f"{slugify(folder.name)}.md"
            if not dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(stub, encoding="utf-8")
            stubs.append(f"category page for {folder.name} (no hub note)")

    write_privacy_nav(notes, dry_run)

    # report
    print("== vault -> site sync ==")
    for name, count in counts.items():
        print(f"  {name:8s} {count:3d} notes")
    for s in stubs:
        print(f"  stub     {s}")
    print(f"  images   {img_count} copied")
    if ctx.unresolved:
        print(f"\n!! {len(ctx.unresolved)} unresolved reference(s):")
        for u in ctx.unresolved:
            print(f"   - {u}")
    else:
        print("  links    all resolved")
    if dry_run:
        print("\n(dry run: nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
