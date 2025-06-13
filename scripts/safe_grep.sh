#!/usr/bin/env bash
set -euo pipefail
# shellcheck source=ci_utils.sh
source "$(dirname "$0")/ci_utils.sh"
limit_output
grep "$@" | cut -b1-200
