#!/bin/bash
set -e
for file in tests/golden_prompts/*.md; do
  basename=$(basename "$file")
  [ "$basename" = "README.md" ] && continue
  echo "Checking $file"
  for section in INPUT EXPECTED NOTES; do
    if ! grep -q "^### .*${section}" "$file"; then
      echo "Missing section $section in $file" >&2
      exit 1
    fi
  done
  if ! grep -q "^**Tags:**" "$file"; then
    echo "Missing Tags in $file" >&2
    exit 1
  fi
done
echo "All golden prompts validated"
