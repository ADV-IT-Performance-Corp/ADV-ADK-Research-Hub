# Config Adjustment Validation
<!-- markdownlint-disable MD001 -->

### INPUT
Update the routing configuration to use `content_agent_v2` and ensure previous tasks remain unaffected.

### EXPECTED
- Shows YAML diff of routing table.
- Invokes ConfigAgent self-reflection on schema change.
- Outputs confirmation of successful validation.

### NOTES
Prompt Kernel: v3.5
**Tags:** config management, schema diff, validation
