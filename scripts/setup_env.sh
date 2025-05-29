#!/usr/bin/env bash
set -euo pipefail

# Install Node.js and tools locally
if ! command -v node >/dev/null; then
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
  apt-get install -y nodejs
fi
npm install -g markdownlint-cli2 >/dev/null

# Install jq and yamllint
apt-get update >/dev/null
apt-get install -y jq yamllint >/dev/null

echo "Environment ready"
