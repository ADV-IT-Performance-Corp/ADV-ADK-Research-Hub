#!/usr/bin/env bash
set -e

for file in tests/golden_prompts/*.md; do
  echo "Validating $file"
  for section in INPUT EXPECTED NOTES; do
    if ! grep -q "^### $section" "$file"; then
      echo "Missing section $section in $file" >&2
      exit 1
    fi
  done
  if ! grep -q "^\*\*Tags:\*\*" "$file"; then
    echo "Missing Tags in $file" >&2
    exit 1
  fi
  if ! grep -q "v3\.5" "$file"; then
    echo "Version not specified in $file" >&2
    exit 1
  fi
  echo "✓ $file valid"
  echo
done
