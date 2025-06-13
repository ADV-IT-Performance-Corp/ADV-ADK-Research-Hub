#!/usr/bin/env bash
set -euo pipefail
grep "$@" | cut -b1-200
