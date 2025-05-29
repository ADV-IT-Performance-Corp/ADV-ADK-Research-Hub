#!/bin/bash
# Setup environment dependencies for local validation
set -e

# Install Node and npm packages if not already available
if ! command -v node >/dev/null 2>&1; then
  echo "Node.js not found. Installing via apt-get..."
  sudo apt-get update && sudo apt-get install -y nodejs npm
fi

# Install markdownlint-cli2
if ! command -v markdownlint-cli2 >/dev/null 2>&1; then
  npm install -g markdownlint-cli2
fi

# Install jq and yamllint
if ! command -v jq >/dev/null 2>&1; then
  sudo apt-get update && sudo apt-get install -y jq
fi
if ! command -v yamllint >/dev/null 2>&1; then
  sudo apt-get update && sudo apt-get install -y yamllint
fi

echo "Environment setup complete."
