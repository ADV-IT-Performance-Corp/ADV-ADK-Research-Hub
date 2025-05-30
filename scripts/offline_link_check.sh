#!/bin/bash
# Simple link checker that works without network access
set -e
missing=0
while read -r url; do
  if ! grep -q "$url" offline_cache 2>/dev/null; then
    echo "WARN: $url not cached" >&2
    missing=1
  fi
done < <(grep -rhoE 'https?://[^ )]+' docs/external | sort -u)
exit $missing
