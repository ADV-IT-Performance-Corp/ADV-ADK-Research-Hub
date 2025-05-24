#!/bin/bash
set -e

# Minimal environment setup
sudo apt-get update
sudo apt-get install -y jq curl || true

echo "✅ Minimal environment setup complete"
