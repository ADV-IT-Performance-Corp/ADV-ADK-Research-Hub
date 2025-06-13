#!/usr/bin/env bash
set -euo pipefail
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output

info "Installing Python 3.11 via pyenv..."
if ! command -v pyenv >/dev/null 2>&1; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev >/dev/null
  curl -fsSL https://pyenv.run | bash
  export PATH="$HOME/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
fi

pyenv install -s 3.11.9
pyenv local 3.11.9

info "Installing Google Cloud CLI..."
GCLOUD_URL="https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-475.0.0-linux-x86_64.tar.gz"
curl -fsSL "$GCLOUD_URL" | tar -xz
./google-cloud-sdk/install.sh --quiet

info "Installing Python packages..."
python3 -m pip install --quiet --upgrade pip
python3 -m pip install --quiet google-adk[cli] google-cloud-aiplatform pre-commit black flake8 mypy

info "Disabling npm and yarn proxy variables..."
if command -v npm >/dev/null 2>&1; then
  npm config delete proxy || true
  npm config delete http-proxy || true
  npm config delete https-proxy || true
fi
if command -v yarn >/dev/null 2>&1; then
  yarn config delete proxy || true
  yarn config delete https-proxy || true
fi
unset npm_config_proxy npm_config_http_proxy npm_config_https_proxy \
  http_proxy https_proxy HTTP_PROXY HTTPS_PROXY

info "Setting up pre-commit hooks..."
pre-commit install --install-hooks

cat <<'EOF'
==============================
✅  Development setup complete
==============================
EOF
