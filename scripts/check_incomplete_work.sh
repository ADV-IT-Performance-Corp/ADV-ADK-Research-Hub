#!/usr/bin/env bash
# Fail CI if documentation contains unfinished sections.
# Extracted from the CI workflow to avoid quoting pitfalls.
set -euo pipefail
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output

echo "Checking for incomplete work..."
matches=$("$(dirname "$0")/safe_grep.sh" -RniE '(TODO|Coming soon|placeholder)' docs/ prompt_catalog/ \
  --include="*.md" --include="*.yaml" --include="*.yml" --exclude-dir=legacy 2>/dev/null \
  | "$(dirname "$0")/safe_grep.sh" -viE '^\s*```|<!--.*-->' || true)
if [ -n "$matches" ]; then
  echo "$matches"
  branch=$(git rev-parse --abbrev-ref HEAD)
  if [ "$branch" = "master" ]; then
    echo "❌ Detected incomplete work on master. Please resolve before merging."
    exit 1
  else
    echo "⚠️ Incomplete work detected on $branch. Proceeding with warning."
  fi
fi
