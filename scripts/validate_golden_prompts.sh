#!/usr/bin/env bash
set -euo pipefail
set -x

# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"

# Read the major/minor version prefix from the VERSION file
VERSION_PREFIX=$(cut -d. -f1-2 VERSION)

info "Validating golden prompts..."
for file in tests/golden_prompts/*.md; do
  if [ "$(basename "$file")" = "README.md" ]; then
    continue
  fi
  info "Checking $file"
  for section in INPUT EXPECTED NOTES; do
    if ! grep -q "^### $section" "$file"; then
      error "Missing section: $section in $file"
      exit 1
    fi
  done
  if ! grep -q '^**Tags:**' "$file"; then
    error "Missing Tags in $file"
    exit 1
  fi
  if ! grep -q "v${VERSION_PREFIX}" "$file"; then
    error "Version not specified or incorrect in $file"
    exit 1
  fi
  info "$file is valid"
done
info "Golden prompt validation complete"
