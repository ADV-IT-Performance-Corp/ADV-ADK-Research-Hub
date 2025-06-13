#!/usr/bin/env bash
# O3 Deep Research shell configuration
# Source this file to enable consistent aliases and terminal settings.

alias grep='grep --color=never'
alias find='find "$@" | cut -b1-200'

export LINES=0
export COLUMNS=0
