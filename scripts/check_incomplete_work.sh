#!/usr/bin/env bash
# Fail CI if documentation contains unfinished sections.
# Extracted from the CI workflow to avoid quoting pitfalls.
set -euo pipefail

echo "Checking for incomplete work..."
matches=$(grep -RniE '(TODO|Coming soon|placeholder)' docs/ --include="*.md" --include="*.yaml" --include="*.yml" --exclude-dir=legacy | grep -viE '^\s*```|<!--.*-->')
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
