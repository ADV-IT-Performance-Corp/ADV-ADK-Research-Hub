#!/usr/bin/env bash
# O3 Deep Research shell configuration
# Source this file to enable consistent aliases and terminal settings.

alias grep='grep --color=never'
find_cut() {
  command find "$@" | cut -b1-200
}
alias find=find_cut

export LINES=0
export COLUMNS=0
