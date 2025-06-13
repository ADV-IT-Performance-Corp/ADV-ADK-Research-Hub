# Config Schema Mutation
<!-- markdownlint-disable MD001 -->

### INPUT
ConfigAgent receives a proposed schema change that alters field types. Summarize the difference and advise if migration steps are required.

### EXPECTED
- Shows before/after schema block with highlights
- Warns if new fields break backward compatibility
- Mentions version 3.5.10 in the notification

### NOTES
Prompt Kernel: v4.0.0
**Tags:** config-agent, schema-mutation
