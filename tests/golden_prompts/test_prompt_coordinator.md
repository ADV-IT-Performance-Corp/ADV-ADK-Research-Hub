# Prompt Coordinator
<!-- markdownlint-disable MD001 -->

### INPUT
Act as a research agent coordinating with campaign and memory agents to optimize a digital ad strategy. Include ReAct-style reasoning and trigger a feedback loop.

### EXPECTED

- Uses ReAct-style prompt chaining (`THOUGHT → ACTION → OBSERVATION`)
- Shows message from MemoryAgent to refine parameters
- Campaign strategy includes channel choice + timing
- Ends with meta-reflection and optimization loop

### NOTES
Prompt Kernel: v3.5.9

**Tags:** multi-agent coordination, ReAct
