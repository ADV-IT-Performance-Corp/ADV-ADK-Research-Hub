#!/usr/bin/env bash
# Validate external HTTP/HTTPS links using markdown-link-check.
# This complements markdownlint and mkdocs which only check formatting and
# internal anchors. Exits non-zero if any links are unreachable.
set -euo pipefail

if ! npx --no-install markdown-link-check --version >/dev/null 2>&1; then
  echo "markdown-link-check is not installed. Run 'npm ci' first." >&2
  exit 1
fi
mlc="npx --no-install markdown-link-check"

config=".github/markdown-link-check-config.json"
files=$(git ls-files '*.md')
missing=0
for file in $files; do
  echo "Checking $file"
  output="$($mlc --quiet -c "$config" "$file")"
  echo "$output"
  if echo "$output" | grep -q '\[✖\]'; then
    echo "Broken links found in $file" >&2
    missing=1
  fi
done

echo "Online link check completed"
exit $missing
