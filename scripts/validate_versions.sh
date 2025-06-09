#!/usr/bin/env bash
# Validate version consistency across repository
set -e

FILE_VERSION=$(tr -d '[:space:]' < VERSION)
failed=0

report_ok() { echo "✅ $1"; }
report_err() { echo "❌ $1"; failed=1; }

# config/settings.yaml check
SETTINGS_VERSION=$(grep -oP '^prompt_version:\s*\K[0-9]+\.[0-9]+\.[0-9]+' config/settings.yaml)
if [ "$SETTINGS_VERSION" = "$FILE_VERSION" ]; then
  report_ok "settings.yaml prompt_version matches $FILE_VERSION"
else
  report_err "settings.yaml prompt_version $SETTINGS_VERSION does not match $FILE_VERSION"
fi

# prompt_genome active entry check
ACTIVE_COUNT=$(jq -r '.prompt_genome.prompts[] | select(.status=="active") | .id' docs/meta/prompt_genome.json | grep -c "v$FILE_VERSION" || true)
if [ "$ACTIVE_COUNT" -gt 0 ]; then
  report_ok "prompt_genome.json has active entry v$FILE_VERSION"
else
  report_err "prompt_genome.json missing active entry v$FILE_VERSION"
fi

# source_index core version check
CORE_VERSION=$(jq -r '.sources[] | select(.type=="core") | .version' docs/source_index.json | head -1)
if [ "$CORE_VERSION" = "$FILE_VERSION" ]; then
  report_ok "source_index.json core version matches $FILE_VERSION"
else
  report_err "source_index.json core version $CORE_VERSION does not match $FILE_VERSION"
fi

# Golden Prompts README check
README_VERSION=$(grep -oP '^# Golden Prompts \(v\K[0-9]+\.[0-9]+\.[0-9]+' tests/golden_prompts/README.md | head -1)
if [ "$README_VERSION" = "$FILE_VERSION" ]; then
  report_ok "golden prompts README version matches $FILE_VERSION"
else
  report_err "golden prompts README version $README_VERSION does not match $FILE_VERSION"
fi

# evaluation_results.json check
JSON_VERSION=$(jq -r '.version' docs/meta/evaluation_results.json)
if [ "$JSON_VERSION" = "$FILE_VERSION" ]; then
  report_ok "evaluation_results.json version matches $FILE_VERSION"
else
  report_err "evaluation_results.json version $JSON_VERSION does not match $FILE_VERSION"
fi

if [ "$failed" -eq 1 ]; then
  exit 1
else
  echo "All version checks passed for $FILE_VERSION"
fi
