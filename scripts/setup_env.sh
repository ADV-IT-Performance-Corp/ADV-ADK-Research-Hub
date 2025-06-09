#!/usr/bin/env bash
set -euo pipefail

packages=()

# Install Node.js v18 if node is missing
if ! command -v node >/dev/null 2>&1; then
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
  packages+=(nodejs)
fi

# Ensure jq and yamllint are installed
for tool in jq yamllint; do
  command -v "$tool" >/dev/null 2>&1 || packages+=("$tool")
done

# Install any missing packages
if [ "${#packages[@]}" -gt 0 ]; then
  apt-get update -qq
  apt-get install -y "${packages[@]}" >/dev/null
fi

# Install markdownlint-cli2 globally if npm exists
if command -v npm >/dev/null 2>&1 && ! command -v markdownlint >/dev/null 2>&1; then
  npm install -g markdownlint-cli2 >/dev/null
fi

echo "Environment ready"
