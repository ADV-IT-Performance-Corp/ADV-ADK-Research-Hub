# Config Schema Diff
<!-- markdownlint-disable MD001 -->

### INPUT
The ConfigAgent receives a new schema with additional fields and modified defaults. Produce a YAML diff and highlight compatibility warnings.

### EXPECTED
- Shows added and removed fields in diff format
- Warns if any required fields are missing
- Sends `config_push` notification referencing version 3.5.10

### NOTES
Prompt Kernel: v3.5.10

**Tags:** config-agent, schema-diff
