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
  DEBIAN_FRONTEND=noninteractive apt-get install -y "${packages[@]}" >/dev/null
fi

# Remove any npm proxy configuration and clear related environment variables
if command -v npm >/dev/null 2>&1; then
  npm config delete proxy || true
  npm config delete http-proxy || true
  npm config delete https-proxy || true
fi
unset npm_config_proxy npm_config_http_proxy npm_config_https_proxy \
  http_proxy https_proxy HTTP_PROXY HTTPS_PROXY

# Propagate cleared variables to subsequent CI steps
if [ -n "${GITHUB_ENV:-}" ]; then
  {
    echo "npm_config_proxy="
    echo "npm_config_http_proxy="
    echo "npm_config_https_proxy="
    echo "http_proxy="
    echo "https_proxy="
    echo "HTTP_PROXY="
    echo "HTTPS_PROXY="
  } >> "$GITHUB_ENV"
fi

# Install markdownlint-cli2 globally if npm exists
if command -v npm >/dev/null 2>&1 && ! command -v markdownlint >/dev/null 2>&1; then
  npm install -g markdownlint-cli2 >/dev/null
fi

echo "Environment ready"
