# Config Adjustment Validation
<!-- markdownlint-disable MD001 -->

### INPUT
The ConfigAgent receives a routing weight update and must produce a diff summary. Include schema context and notify via `config_push` message.

### EXPECTED
- Shows YAML diff with before/after sections
- Sends `config_push` notification to other agents
- References version 3.5.5 in output

### NOTES
Prompt Kernel: v3.5.7

**Tags:** config-agent, schema-diff
