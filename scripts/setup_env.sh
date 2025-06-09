#!/usr/bin/env bash
set -euo pipefail

# Install Node.js and tools locally only if missing
SUDO=""
if [ "$(id -u)" -ne 0 ]; then
  if command -v sudo >/dev/null 2>&1; then
    SUDO="sudo"
  else
    echo "This script requires root privileges (sudo missing)." >&2
    exit 1
  fi
fi

packages=()

# Node.js 18 is required
need_node=false
if command -v node >/dev/null && command -v npm >/dev/null; then
  node_major=$(node -v | sed -E 's/^v([0-9]+).*/\1/')
  if [ "$node_major" -lt 18 ]; then
    need_node=true
  fi
else
  need_node=true
fi

if [ "$need_node" = true ]; then
  curl -fsSL https://deb.nodesource.com/setup_18.x | $SUDO -E bash -
  packages+=(nodejs)
fi

if ! command -v jq >/dev/null; then
  packages+=(jq)
fi

if ! command -v yamllint >/dev/null; then
  packages+=(yamllint)
fi

if [ ${#packages[@]} -gt 0 ]; then
  $SUDO apt-get update -qq
  DEBIAN_FRONTEND=noninteractive $SUDO apt-get install -y --no-install-recommends "${packages[@]}" >/dev/null
fi

if command -v npm >/dev/null; then
  if ! command -v markdownlint-cli2 >/dev/null; then
    npm install -g markdownlint-cli2 >/dev/null
  fi
fi

echo "Environment ready"
