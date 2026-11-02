# eugenetl.com — TL;DR / Eugene's Tech Lab

Personal site: HTB & CTF writeups, privacy guides, projects, CV and portfolio.
Content is written in **Obsidian** and published here with one command.

## How publishing works

The website content is **generated** from the Obsidian vaults — never edit
`_HTB/`, `_CTF/`, `_privacy_docs/` or `assets/content/` by hand.

```
Obsidian vaults                          this repo
──────────────────────────────           ────────────────────────────
Cysec Notes/04 - Writeups/
├── HTB/Released/…            ──┐
└── CTF/Released/…            ──┤  tools/sync.py
Personal notes/Privacy Tools/  │        (rewrites frontmatter, converts
└── Released/…               ──┘         ![[embeds]] and [[wikilinks]])
                                        _HTB/  _CTF/  _privacy_docs/
```

**Publish rule: folder-based, allowlist-only.** Anything under a `Released/`
folder is published; anything under `Unreleased/` is never even read by the
sync script. Moving a note folder from `Unreleased/` to `Released/` is the act
of publishing it.

On the website copy the sync script:

- drops vault bookkeeping frontmatter (emoji `tags:`, `tasks`, `priority`, …)
  and derives site tags from metadata (platform, OS, difficulty, event);
- rewrites `![[image.png]]` into real `<img>` tags and copies the images;
- rewrites `[[wikilink]]` into links **only when the target is published** —
  links to unpublished notes render as plain text, so nothing leaks;
- skips `*.excalidraw.md` and templates.

Vault notes are never modified.

## Publishing (day to day)

```sh
./publish.sh                # sync vaults -> commit -> push (CI deploys)
./publish.sh --preview      # sync + jekyll serve at http://localhost:4000
./publish.sh --build        # sync + build _site locally
./publish.sh --sync         # sync only
```

Requires `python3` + PyYAML (`pip install --user pyyaml`) and Ruby + Bundler
for local builds. Deployment is automatic: pushing to `main` triggers
`.github/workflows/deploy.yml`, which builds with Jekyll and deploys to
GitHub Pages (custom domain: `CNAME`).

## Repo layout

| Path | Purpose |
|---|---|
| `tools/sync.py`, `tools/sync.yml` | vault → site sync (sources & publish rules) |
| `publish.sh` | one-command publish flow |
| `_HTB/`, `_CTF/`, `_privacy_docs/` | **generated** content collections |
| `assets/content/` | **generated** images |
| `_layouts/`, `_includes/`, `_sass/`, `assets/` | theme (edit freely) |
| `index.html`, `writeups/`, `privacy/`, `projects/`, `portfolio/`, `about/` | site pages |
| `_data/cv.yml`, `_data/projects.yml`, `_data/portfolio.yml` | editable content (CV, projects, portfolio) |

## Notes

- URLs are built from vault folder paths, e.g. `HTB/Released/season4/bizness.md`
  → `/writeups/htb/season4/bizness/`, `CTF/Released/2026/BKCTF/Tiny SQL.md`
  → `/writeups/ctf/2026/bkctf/tiny-sql/`.
- A CTF event overview note named like its folder (`BKCTF/BKCTF.md`,
  `0xFUN/0xFUN CTF.md`) becomes the event landing page.
- Writeup content is wrapped in `{% raw %}` so payloads like `{{7*7}}` stay
  literal.
- GitHub → Settings → Pages → Source must be **"GitHub Actions"**.
