#!/usr/bin/env bash
set -euo pipefail
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output

# Preserve existing proxy settings so they can be restored after npm steps
ORIG_HTTP_PROXY="${http_proxy-}"
ORIG_HTTPS_PROXY="${https_proxy-}"
ORIG_HTTP_PROXY_UPPER="${HTTP_PROXY-}"
ORIG_HTTPS_PROXY_UPPER="${HTTPS_PROXY-}"

packages=()

# Install Node.js 18.x if node is missing
if ! command -v node >/dev/null 2>&1; then
  NODE_SCRIPT_URL="https://deb.nodesource.com/setup_18.x"
  TMP_SCRIPT=$(mktemp)
  curl -fsSL "$NODE_SCRIPT_URL" -o "$TMP_SCRIPT"
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

# Install markdownlint-cli2 globally if npm exists
if command -v npm >/dev/null 2>&1 && ! command -v markdownlint >/dev/null 2>&1; then
  npm install -g markdownlint-cli2 >/dev/null
fi

# Restore saved proxy variables so later commands inherit them
export http_proxy="$ORIG_HTTP_PROXY"
export https_proxy="$ORIG_HTTPS_PROXY"
export HTTP_PROXY="$ORIG_HTTP_PROXY_UPPER"
export HTTPS_PROXY="$ORIG_HTTPS_PROXY_UPPER"

# Propagate cleared variables to subsequent CI steps
if [ -n "${GITHUB_ENV:-}" ]; then
  {
    echo "npm_config_proxy="
    echo "npm_config_http_proxy="
    echo "npm_config_https_proxy="
    echo "http_proxy=$http_proxy"
    echo "https_proxy=$https_proxy"
    echo "HTTP_PROXY=$HTTP_PROXY"
    echo "HTTPS_PROXY=$HTTPS_PROXY"
  } >> "$GITHUB_ENV"
fi

echo "Environment ready"
