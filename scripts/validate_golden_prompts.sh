#!/bin/bash
set -e
STATUS=0
for file in tests/golden_prompts/*.md; do
  [ "$(basename $file)" = "README.md" ] && continue
  echo "Checking $file"
  for section in INPUT EXPECTED NOTES; do
    if ! grep -q "^### .*${section}" "$file"; then
      echo "Missing section $section in $file"
      STATUS=1
    fi
  done
  if ! grep -q "^**Tags:**" "$file"; then
    echo "Missing Tags in $file"
    STATUS=1
  fi
  if ! grep -q "v3\.5" "$file"; then
    echo "Incorrect version in $file"
    STATUS=1
  fi
done
exit $STATUS
