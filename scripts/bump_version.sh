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
echo "${new}" > VERSION

# Update prompt version in settings.yaml
sed -i "s/^prompt_version: .*/prompt_version: ${new}/" config/settings.yaml

# Update meta evaluation if old version referenced without leading 'v'
if [ -f docs/meta/meta_evaluation.json ]; then
  sed -i "s/${old}/${new}/g" docs/meta/meta_evaluation.json
fi

# Update changelog placeholder if present
if grep -q "^## \[Unreleased\]" CHANGELOG.md; then
  today=$(date +%Y-%m-%d)
  sed -i "0,/^## \[Unreleased\]/s//## [v${new}] — ${today}/" CHANGELOG.md
fi
echo "Bumped version from ${old} to ${new}"
