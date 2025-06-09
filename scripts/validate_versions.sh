#!/usr/bin/env bash
set -euo pipefail

FILE_VERSION=$(tr -d '[:space:]' < VERSION)

echo "Checking version consistency across repository..."

echo "VERSION file => $FILE_VERSION"

errors=0

SETTINGS_VERSION=$(grep -oP '^prompt_version:\s*\K[0-9]+\.[0-9]+\.[0-9]+' config/settings.yaml)
if [ "$SETTINGS_VERSION" != "$FILE_VERSION" ]; then
  echo "❌ settings.yaml has $SETTINGS_VERSION but VERSION is $FILE_VERSION"
  errors=1
else
  echo "✅ settings.yaml matches VERSION"
fi

ACTIVE_COUNT=$(jq -r '.prompt_genome.prompts[] | select(.status=="active") | .id' docs/meta/prompt_genome.json | grep -c "v$FILE_VERSION" || true)
if [ "$ACTIVE_COUNT" -eq 0 ]; then
  echo "❌ No active prompt_genome entry for version $FILE_VERSION"
  errors=1
else
  echo "✅ prompt_genome.json has active entry for $FILE_VERSION"
fi

CORE_VERSION=$(jq -r '.sources[] | select(.type=="core") | .version' docs/source_index.json | head -1)
if [ "$CORE_VERSION" != "$FILE_VERSION" ]; then
  echo "❌ docs/source_index.json core version $CORE_VERSION does not match VERSION $FILE_VERSION"
  errors=1
else
  echo "✅ docs/source_index.json core version matches VERSION"
fi

README_VERSION=$(grep -oP 'version-\K[0-9]+\.[0-9]+\.[0-9]+' README.md | head -1)
if [ "$README_VERSION" != "$FILE_VERSION" ]; then
  echo "❌ README.md version $README_VERSION does not match VERSION $FILE_VERSION"
  errors=1
else
  echo "✅ README.md version matches VERSION"
fi

GP_VERSION=$(grep -oP 'Golden Prompts \(v\K[0-9]+\.[0-9]+\.[0-9]+' tests/golden_prompts/README.md | head -1)
if [ "$GP_VERSION" != "$FILE_VERSION" ]; then
  echo "❌ Golden Prompts README version $GP_VERSION does not match VERSION $FILE_VERSION"
  errors=1
else
  echo "✅ Golden Prompts README matches VERSION"
fi

if [ -f docs/meta/evaluation_results.json ]; then
  JSON_VERSION=$(jq -r '.version' docs/meta/evaluation_results.json)
  if [ "$JSON_VERSION" != "$FILE_VERSION" ]; then
    echo "❌ evaluation_results.json version $JSON_VERSION does not match VERSION $FILE_VERSION"
    errors=1
  else
    echo "✅ evaluation_results.json version matches VERSION"
  fi
fi

if [ "$errors" -ne 0 ]; then
  exit 1
fi

echo "✅ All versions match $FILE_VERSION"
