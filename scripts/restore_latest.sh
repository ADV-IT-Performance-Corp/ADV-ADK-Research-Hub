#!/usr/bin/env bash
set -euo pipefail
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output

info "Fetching latest backup branch..."
git fetch origin "backup/*" >/dev/null
latest=$(git for-each-ref --sort=-creatordate --format='%(refname:strip=2)' refs/remotes/origin/backup | head -n1)

if [ -z "$latest" ]; then
  error "No backup branches found"
  exit 1
fi

info "Fast-forwarding master to $latest"
git checkout master
git merge --ff-only "origin/$latest"

info "Running validation scripts"
bash scripts/validate_yaml.sh
bash scripts/check_incomplete_work.sh
bash scripts/validate_versions.sh

info "Restore complete"
