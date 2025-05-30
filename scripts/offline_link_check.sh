#!/usr/bin/env bash
# Basic offline link validation using a cached list.
# Links not in cache are skipped with a warning.

CACHE="scripts/link_cache.txt"
if [ ! -f "$CACHE" ]; then
  echo "No cache file found at $CACHE" >&2
  exit 0
fi

links=$(grep -rEo 'https?://[^\") >]+' docs/ README.md | grep -v 'localhost\|example.com' | sort -u)

while read -r url; do
  status=$(grep "^$url " "$CACHE" | awk '{print $2}')
  if [ -z "$status" ]; then
    echo "⚠️  No cache entry for $url" >&2
    continue
  fi
  if [ "$status" != "200" ]; then
    echo "❌ Cached bad link: $url" >&2
    exit 1
  else
    echo "✅ $url"
  fi
done <<< "$links"
