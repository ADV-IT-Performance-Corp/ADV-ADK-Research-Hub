#!/usr/bin/env bash
set -euo pipefail
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output

# Install Python 3.11 via pyenv
if ! command -v pyenv >/dev/null 2>&1; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev > /dev/null
  curl https://pyenv.run | bash
  export PATH="$HOME/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
fi

pyenv install -s 3.11.9
pyenv local 3.11.9

# Install gcloud CLI
URL=https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-475.0.0-linux-x86_64.tar.gz
curl -fsSL "$URL" | tar -xz
./google-cloud-sdk/install.sh --quiet

# Install ADK CLI via pipx
if ! command -v pipx >/dev/null 2>&1; then
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath
  export PATH="$HOME/.local/bin:$PATH"
fi
pipx install google-adk[cli]

# Export GCP_PROJECT
if ! grep -q 'GCP_PROJECT' ~/.bashrc; then
  echo 'export GCP_PROJECT=<your-gcp-project>' >> ~/.bashrc
fi

echo "Development environment ready"
