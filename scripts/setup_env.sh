#!/usr/bin/env bash
set -euo pipefail

# Install Node.js and tools locally only if missing
packages=()
if ! command -v node >/dev/null || ! command -v npm >/dev/null; then
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
  packages+=(nodejs)
fi
if ! command -v jq >/dev/null; then
  packages+=(jq)
fi
if ! command -v yamllint >/dev/null; then
  packages+=(yamllint)
fi
if [ ${#packages[@]} -gt 0 ]; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y "${packages[@]}" >/dev/null
fi

if command -v npm >/dev/null; then
  npm install -g markdownlint-cli2 >/dev/null
fi

echo "Environment ready"
