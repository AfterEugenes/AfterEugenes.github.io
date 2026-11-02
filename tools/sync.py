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
import os
import posixpath
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
RE_WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+?)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]")
RE_HIGHLIGHT = re.compile(r"==([^=\n]+)==")
RE_FENCE = re.compile(r"^(```|~~~)")
RE_INLINE_CODE = re.compile(r"(`[^`]*`)")
RE_CALLOUT = re.compile(r"^>\s*\[!([a-zA-Z-]+)\]([+-]?)\s*(.*)$")
RE_FM_KEY = re.compile(r"^([A-Za-z0-9 _-]+):")


# ---------------------------------------------------------------- utilities

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def load_config() -> dict:
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    for key, value in cfg.get("vault_roots", {}).items():
        cfg.setdefault("_roots", {})[key] = value
    # expand {vault} placeholders
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
    return fallback.isoformat(timespec="minutes")


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

    def resolve(self, ref: str, note: Path) -> Path | None:
        ref = ref.strip()
        cands = self.by_name.get(posixpath.basename(ref).lower(), [])
        if not cands:
            return None
        same_dir = [c for c in cands if note.parent in c.parents]
        if same_dir:
            return same_dir[0]
        if "/" in ref:
            exact = [c for c in cands if c.as_posix().endswith(ref)]
            if exact:
                return exact[0]
        return cands[0]


# -------------------------------------------------------------------- notes

class Note:
    def __init__(self, src: dict, path: Path):
        self.src = src
        self.path = path
        self.rel = path.relative_to(src["root"])
        self.parts = self.rel.with_suffix("").parts
        self.slugs = [slugify(p) for p in self.parts]
        self.platform = src["platform"]

        # event overview candidate: note named like its folder (BKCTF/BKCTF.md,
        # 0xFUN/0xFUN CTF.md). The actual overview is elected after collection.
        self.overview_candidate = (
            src["platform"] == "ctf"
            and len(self.slugs) >= 2
            and (self.slugs[-1] == self.slugs[-2]
                 or self.slugs[-1] in (self.slugs[-2] + "-ctf", self.slugs[-2] + "-writeups"))
        )
        self.kind = "note"
        self.url = src["url_prefix"] + "/" + "/".join(self.slugs) + "/"

        self.fm, self.body = split_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        # drop control characters (NUL bytes survive in some vault notes)
        self.body = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", self.body)
        self.warnings: list[str] = []

        # folder-derived metadata
        self.year = self.parts[0] if self.platform == "ctf" and len(self.parts) >= 2 else None
        self.event = self.parts[-2] if self.platform == "ctf" and len(self.parts) >= 2 else None
        self.season = None
        if self.platform == "htb" and len(self.parts) >= 2:
            m = re.search(r"(\d+)", self.parts[0])
            self.season = m.group(1) if m else self.parts[0]
        self.category = self.parts[0] if self.platform == "privacy" and len(self.parts) >= 2 else "General"

        self.title = str(self.fm.get("title") or self.parts[-1]).strip()
        desc = self.fm.get("description") or self.fm.get("Description") or ""
        self.description = str(desc).strip()
        self.date = normalize_date(self.fm.get("date"), dt.datetime.fromtimestamp(path.stat().st_mtime))

        # images copied for this note: basename -> site url
        self.images: dict[str, str] = {}

    def meta(self, prev_url: str | None, next_url: str | None) -> dict:
        m: dict = {
            "layout": "ctf-event" if self.kind == "event-overview" else self.src["layout"],
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

        # derived tags (vault emoji tags are dropped on purpose)
        tags = list(self.src.get("derive_tags", []))
        if self.platform == "htb":
            for v in (self.fm.get("os"), self.fm.get("difficulty")):
                if v and str(v).strip() and str(v).strip().lower() not in [t.lower() for t in tags]:
                    tags.append(str(v).strip().lower())
        elif self.platform == "ctf":
            if self.year and str(self.year) not in tags:
                tags.append(str(self.year))
        elif self.platform == "privacy":
            if self.category != "General" and self.category not in tags:
                tags.append(self.category)
        m["tags"] = tags

        if prev_url:
            m["prev_url"] = prev_url
        if next_url:
            m["next_url"] = next_url
        return m


# --------------------------------------------------------------- transforms

def transform_body(note: Note, link_index: dict[str, str], img_index: ImageIndex,
                   unresolved: list[str]) -> str:
    out_lines: list[str] = []
    lines = note.body.splitlines()
    i = 0
    in_fence = False

    def handle_embed(line: str) -> str:
        def rep(m: re.Match) -> str:
            ref, _anchor, size = m.group(1).strip(), m.group(2), m.group(3)
            # excalidraw drawing: try an exported image first
            if ref.lower().endswith(".excalidraw"):
                export = img_index.resolve(ref.rsplit(".", 1)[0] + ".png", note.path)
                if export:
                    ref = export.name
                else:
                    unresolved.append(f"{note.rel}: dropped drawing embed '![[{ref}]]'")
                    return ""
            img = img_index.resolve(ref, note.path)
            if img is None:
                unresolved.append(f"{note.rel}: missing image '![[{ref}]]'")
                return ""
            if img.name not in note.images:
                # one folder per note, derived from its vault path
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
            alt = html.escape(re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", alt), quote=True)
            return (f'<img class="content-image" src="{note.images[img.name]}"'
                    f' alt="{alt}" loading="lazy"{attrs}>')

        return RE_EMBED.sub(rep, line)

    def handle_links(line: str) -> str:
        def rep(m: re.Match) -> str:
            target, anchor, alias = m.group(1).strip(), m.group(2), m.group(3)
            key = re.sub(r"\.(md|markdown)$", "", target, flags=re.I).strip().lower()
            url = link_index.get(key)
            text = (alias or target).strip()
            if url is None:
                unresolved.append(f"{note.rel}: link to unpublished note '[[{target}]]' shown as text")
                return f'<span class="obsidian-link-missing" title="Not published">{text}</span>'
            if anchor:
                url += "#" + slugify(anchor)
            return f'<a class="obsidian-link" href="{url}">{text}</a>'

        return RE_WIKILINK.sub(rep, line)

    def handle_highlights(line: str) -> str:
        return RE_HIGHLIGHT.sub(r"<mark>\1</mark>", line)

    def convert_part(part: str) -> str:
        part = handle_embed(part)
        part = handle_links(part)
        part = handle_highlights(part)
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
        parts = RE_INLINE_CODE.split(line)
        out_lines.append("".join(p if p.startswith("`") and p.endswith("`") and len(p) > 1
                                 else convert_part(p) for p in parts))
        i += 1

    return "\n".join(out_lines)


# --------------------------------------------------------------------- main

def main() -> int:
    dry_run = "--dry-run" in sys.argv
    cfg = load_config()

    img_index = ImageIndex(cfg["image_search_roots"])
    unresolved: list[str] = []

    notes: list[Note] = []
    stubs: list[dict] = []
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
        winner.url = winner.src["url_prefix"] + "/" + "/".join(winner.slugs[:-1]) + "/"

    # link index: title + file stem (+ aliases) -> url
    link_index: dict[str, str] = {}
    for n in notes:
        for key in [n.title, n.parts[-1], *(n.fm.get("aliases") or [])]:
            link_index.setdefault(str(key).strip().lower(), n.url)

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
        body = transform_body(n, link_index, img_index, unresolved)
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
        stubs.append({"event": event, "year": year})

    # report
    print("== vault -> site sync ==")
    for name, count in counts.items():
        print(f"  {name:8s} {count:3d} notes")
    for s in stubs:
        print(f"  stub     event page generated for {s['event']} {s['year']} (no overview note)")
    print(f"  images   {img_count} copied")
    if unresolved:
        print(f"\n!! {len(unresolved)} unresolved reference(s):")
        for u in unresolved:
            print(f"   - {u}")
    else:
        print("  links    all resolved")
    if dry_run:
        print("\n(dry run: nothing written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
