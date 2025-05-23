#!/bin/bash
set -e
for file in tests/golden_prompts/*.md; do
  echo "Validating $file"
  grep -q '^### INPUT' "$file" || { echo "Missing INPUT in $file"; exit 1; }
  grep -q '^### EXPECTED' "$file" || { echo "Missing EXPECTED in $file"; exit 1; }
  grep -q '^### NOTES' "$file" || { echo "Missing NOTES in $file"; exit 1; }
  grep -q '^**Tags:**' "$file" || { echo "Missing Tags in $file"; exit 1; }
  echo "$file OK"
done
