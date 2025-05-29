#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <old_version> <new_version>" >&2
  exit 1
fi
old=$1
new=$2

files=(README.md tests/golden_prompts/README.md .github/pull_request_template.md .github/workflows/validate_repo.yml)

for f in "${files[@]}"; do
  if [ -f "$f" ]; then
    sed -i "s/$old/$new/g" "$f"
  fi
done

# Prepend new entry to CHANGELOG
sed -i "1i ## [v$new] — $(date +%Y-%m-%d)\n\n### ✨ Updates\n- Version bump from $old to $new\n" CHANGELOG.md

echo "Updated version references from $old to $new"
