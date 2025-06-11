#!/bin/bash

set -e

log() {
  echo -e "\033[1;36m[SETUP]\033[0m $1"
}

log "🚀 Starting environment setup for ADV-ADK-Research-Hub..."

# Install base packages only if key tools are missing
MISSING=false
for tool in node npm jq yamllint; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    MISSING=true
    break
  fi
done

if [ "$MISSING" = true ]; then
  log "Installing base system packages..."
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl git python3 python3-pip python3-venv nodejs npm jq yamllint > /dev/null
else
  log "Required tools already installed, skipping package install."
fi

log "✅ Node.js version: $(node -v)"
log "✅ npm version: $(npm -v)"
log "✅ Python version: $(python3 --version)"
log "✅ jq version: $(jq --version)"
log "✅ yamllint version: $(yamllint --version)"

log "Installing markdownlint-cli2 (via npm)..."
npm install --save-dev markdownlint-cli2 markdownlint-cli2-formatter-junit || true
log "✅ markdownlint-cli2 version: $(npx markdownlint-cli2 --version || echo 'not found')"

if [ -f requirements.txt ]; then
  log "Setting up Python virtual environment..."
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
else
  log "⚠️ No requirements.txt found — skipping Python setup."
fi

if [ -f package.json ]; then
  log "Installing Node.js dependencies..."
  HTTP_PROXY= http_proxy= HTTPS_PROXY= https_proxy= \
  npm_config_http_proxy= npm_config_https_proxy= npm_config_proxy= \
  npm ci --omit=optional || npm install
else
  log "⚠️ No package.json found — skipping Node.js installation."
fi

run_if_defined() {
  local name="$1"
  if [ -f package.json ] && jq -e ".scripts[\"$name\"]" package.json > /dev/null 2>&1; then
    log "▶ Running npm script: $name"
    npm run "$name"
  else
    log "ℹ️ Skipping script '$name' — not defined."
  fi
}

run_if_defined lint
run_if_defined test
run_if_defined build

if [ -f ./scripts/init.sh ]; then
  log "Executing scripts/init.sh..."
  chmod +x ./scripts/init.sh
  ./scripts/init.sh
fi

log "✅ Environment fully initialized. CI tools and agent test infra are ready."

