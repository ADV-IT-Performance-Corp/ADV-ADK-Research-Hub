#!/usr/bin/env bash
# Online link check using markdown-link-check
set -euo pipefail

strict=${STRICT_LINKS:-0}
if [[ "${1:-}" == "--strict" ]]; then
  strict=1
elif [[ "${1:-}" == "--warn-only" ]]; then
  strict=0
elif [[ -n "${1:-}" ]]; then
  echo "Usage: $0 [--strict|--warn-only]" >&2
  exit 2
fi

config=".github/markdown-link-check-config.json"
files=$(git ls-files '*.md')
missing=0
for file in $files; do
  echo "Checking $file"
  if ! npx markdown-link-check -q -c "$config" "$file"; then
    echo "Broken links found in $file" >&2
    missing=1
  fi
done

echo "Online link check completed"
if [ "$strict" -eq 1 ]; then
  exit $missing
else
  exit 0
fi
