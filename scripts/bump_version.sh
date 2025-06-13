#!/usr/bin/env bash
# Bump version across docs
set -e
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output
if [ -z "$1" ]; then
  echo "Usage: $0 <new_version>" >&2
  exit 1
fi
old=$("$(dirname "$0")/safe_grep.sh" -m1 -oE 'version-[0-9]+\.[0-9]+\.[0-9]+' README.md | cut -d- -f2)
new="$1"
perl -0pi -e "s/version-${old}/version-${new}/g" README.md
"$(dirname "$0")/safe_grep.sh" -rl "v${old}" docs | xargs sed -i "s/v${old}/v${new}/g"
sed -i "s/${old}/${new}/g" docs/source_index.json
echo "${new}" > VERSION

# Update agent module versions
"$(dirname "$0")/safe_grep.sh" -rl "__version__ =" o3research/agents marketing_assistant \
  | xargs sed -i "s/__version__ = \"${old}\"/__version__ = \"${new}\"/g"

# Update prompt version in settings.yaml
sed -i "s/^prompt_version: .*/prompt_version: ${new}/" config/settings.yaml

# Update meta evaluation if old version referenced without leading 'v'
if [ -f docs/meta/meta_evaluation.json ]; then
  sed -i "s/${old}/${new}/g" docs/meta/meta_evaluation.json
fi

# Update changelog placeholder if present
if "$(dirname "$0")/safe_grep.sh" -q "^## \[Unreleased\]" CHANGELOG.md; then
  today=$(date +%Y-%m-%d)
  sed -i "0,/^## \[Unreleased\]/s//## [v${new}] — ${today}/" CHANGELOG.md
fi
echo "Bumped version from ${old} to ${new}"
