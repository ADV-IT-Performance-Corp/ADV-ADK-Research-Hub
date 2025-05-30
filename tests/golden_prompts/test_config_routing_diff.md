# Config Routing Diff
<!-- markdownlint-disable MD001 -->

### INPUT
ConfigAgent receives a new routing table with updated weights. Provide a summary diff and alert via `config_push`.

### EXPECTED
- Outputs YAML diff highlighting weight changes
- Sends `config_push` message noting version 3.5.5
- Mentions validation checklist

### NOTES
Prompt Kernel: v3.5.5
**Tags:** config-agent, routing-diff
