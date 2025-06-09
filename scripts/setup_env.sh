#!/usr/bin/env bash
set -euo pipefail

packages=()

# Install Node.js v18.20.0 if node is missing
if ! command -v node >/dev/null 2>&1; then
  NODE_SCRIPT_URL="https://deb.nodesource.com/setup_18.20.0"
  TMP_SCRIPT=$(mktemp)
  curl -fsSL "$NODE_SCRIPT_URL" -o "$TMP_SCRIPT"
  EXPECTED_SHA="ed44586adc96bd3e7707abe7659d585dd2e78c67d779bd175273b99bd07a099e"
  ACTUAL_SHA=$(sha256sum "$TMP_SCRIPT" | awk '{print $1}')
  if [ "$ACTUAL_SHA" != "$EXPECTED_SHA" ]; then
    echo "Checksum mismatch for Node.js installer" >&2
    exit 1
  fi
  bash "$TMP_SCRIPT"
  rm "$TMP_SCRIPT"
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
