#!/usr/bin/env bash
# Offline link check using cached status file
set -e
CACHE_FILE="docs/link_cache.txt"
missing=0
if [ ! -f "$CACHE_FILE" ]; then
  echo "Cache file $CACHE_FILE not found" >&2
  exit 1
fi
links=$(grep -rhoE 'https?://[^ )]+' docs/external | sort -u)
for link in $links; do
  status=$(grep -F "$link" "$CACHE_FILE" | head -n 1 | awk '{print $2}')
  if [ -z "$status" ]; then
    echo "WARN: $link not in cache" >&2
    missing=1
  elif [ "$status" != "200" ]; then
    echo "WARN: $link cached status $status" >&2
    missing=1
  fi
done
exit $missing
