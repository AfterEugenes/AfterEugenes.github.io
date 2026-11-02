#!/usr/bin/env bash
# Publish flow: Obsidian vault -> site -> GitHub Pages
#
#   ./publish.sh              sync vaults, commit and push (Actions deploys)
#   ./publish.sh --preview    sync vaults and serve locally at localhost:4000
#   ./publish.sh --build      sync vaults and build _site locally
#   ./publish.sh --sync       sync vaults only (no git)
set -euo pipefail
cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"
if ! "$PYTHON" -c "import yaml" 2>/dev/null; then
  echo "PyYAML missing: python3 -m pip install --user --break-system-packages pyyaml" >&2
  exit 1
fi

"$PYTHON" tools/sync.py

case "${1:-}" in
  --sync) exit 0 ;;
  --preview) exec bundle exec jekyll serve --livereload ;;
  --build) exec bundle exec jekyll build ;;
esac

git add -A
if git diff --cached --quiet; then
  echo "Nothing to publish."
  exit 0
fi
git commit -m "publish: $(date +'%F %H:%M')"
git push
echo "Pushed. GitHub Actions builds and deploys the site."
