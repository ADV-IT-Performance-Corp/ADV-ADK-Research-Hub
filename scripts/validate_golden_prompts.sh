#!/usr/bin/env bash
set -e
for file in tests/golden_prompts/*.md; do
  [ "$file" = "tests/golden_prompts/README.md" ] && continue
  echo "Checking $file"
  for section in INPUT EXPECTED NOTES; do
    if ! grep -q "^###.*$section" "$file"; then
      echo "Missing section: $section in $file" >&2
      exit 1
    fi
  done
  if ! grep -q '^**Tags:**' "$file"; then
    echo "Missing Tags in $file" >&2
    exit 1
  fi
  echo "OK: $file"
done
