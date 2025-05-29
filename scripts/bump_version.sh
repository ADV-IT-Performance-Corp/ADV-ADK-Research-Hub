#!/usr/bin/env bash
# Bump version across docs
set -e
if [ -z "$1" ]; then
  echo "Usage: $0 <new_version>" >&2
  exit 1
fi
old=$(grep -m1 -oE 'version-[0-9]+\.[0-9]+\.[0-9]+' README.md | cut -d- -f2)
new="$1"
perl -0pi -e "s/version-${old}/version-${new}/g" README.md
grep -rl "v${old}" docs | xargs sed -i "s/v${old}/v${new}/g"
sed -i "s/${old}/${new}/g" docs/source_index.json
echo "Bumped version from ${old} to ${new}"
