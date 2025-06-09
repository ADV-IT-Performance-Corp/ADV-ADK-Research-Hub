#!/usr/bin/env bash
# Validate YAML files using yamllint.
# Extracted from the CI workflow to simplify quoting.
set -euo pipefail

CONFIG='{ extends: default, rules: {line-length: {max: 120, allow-non-breakable-inline-mappings: true}} }'

echo "Validating YAML files..."
find . -path ./node_modules -prune -o \( -name '*.yaml' -o -name '*.yml' \) -print0 | xargs -0 yamllint -d "$CONFIG"
