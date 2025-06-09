#!/usr/bin/env bash
# Offline link check using cached status file
set -e

# offline check defaults to warn-only mode. use STRICT_LINKS=1 or --strict to
# make warnings fail the build.
strict=${STRICT_LINKS:-0}

if [ "$1" = "--strict" ]; then
  strict=1
elif [ "$1" = "--warn-only" ]; then
  strict=0
elif [ -n "$1" ]; then
  echo "Usage: $0 [--strict|--warn-only]" >&2
  exit 2
fi

CACHE_FILE="docs/link_cache.txt"
missing=0
if [ ! -f "$CACHE_FILE" ]; then
  echo "Cache file $CACHE_FILE not found" >&2
  exit 1
fi
links=$(grep -rhoP "https?://[^ )\"\\',]+" docs/external | sort -u)
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
if [ "$strict" -eq 1 ]; then
  exit $missing
else
  exit 0
fi
