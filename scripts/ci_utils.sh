#!/usr/bin/env bash

info() {
  printf '\033[32m[INFO]\033[0m %s\n' "$*"
}

warn() {
  printf '\033[33m[WARN]\033[0m %s\n' "$*"
}

error() {
  printf '\033[31m[ERROR]\033[0m %s\n' "$*" >&2
}

# Limit stdout/stderr output to avoid noisy CI logs
limit_output() {
  local bytes="${1:-1600}"
  # shellcheck disable=SC2094
  exec > >(head -c "$bytes")
  exec 2> >(head -c "$bytes" >&2)
}
