#!/usr/bin/env bash
set -euo pipefail

# Read the major/minor version prefix from the VERSION file
VERSION_PREFIX=$(cut -d. -f1-2 VERSION)

echo "Validating golden prompts..."
for file in tests/golden_prompts/*.md; do
  if [ "$(basename "$file")" = "README.md" ]; then
    continue
  fi
  echo "Checking $file"
  for section in INPUT EXPECTED NOTES; do
    if ! grep -q "^### $section" "$file"; then
      echo "Missing section: $section in $file" >&2
      exit 1
    fi
  done
  if ! grep -q '^**Tags:**' "$file"; then
    echo "Missing Tags in $file" >&2
    exit 1
  fi
  if ! grep -q "v${VERSION_PREFIX}" "$file"; then
    echo "Version not specified or incorrect in $file" >&2
    exit 1
  fi
  echo "$file is valid"
done
