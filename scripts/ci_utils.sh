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
