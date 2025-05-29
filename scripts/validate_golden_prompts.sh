#!/bin/bash
# Validate golden prompt markdown files
set -e

dir="tests/golden_prompts"
for file in "$dir"/*.md; do
  echo "Validating $file"
  # Required sections
  for section in "INPUT" "EXPECTED" "NOTES"; do
    if ! grep -q "^### .$section" "$file"; then
      echo "Missing section $section in $file"
      exit 1
    fi
  done

  # Tags line
  if ! grep -q '^\*\*Tags:\*\*' "$file"; then
    echo "Missing or incorrectly formatted Tags in $file"
    exit 1
  fi

  # Version reference
  if ! grep -q 'v3\.5' "$file"; then
    echo "Version not specified or incorrect in $file"
    exit 1
  fi

  echo "$file valid"
done
