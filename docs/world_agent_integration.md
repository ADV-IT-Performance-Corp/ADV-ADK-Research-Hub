# World Agent Integration Blueprint

This guide outlines how external agents can interface with the ADK repository and participate in the multi-agent workflow.

## Goals
- Provide a consistent entry point for "agents of the world" to leverage ADK assets.
- Document the event bus topics and memory patterns used for coordination.
- Ensure updates remain version-controlled through the Prompt Genome and CI checks.

## Integration Steps
1. **Repository Access** — Connect via GitHub or clone the repo locally. Reference key files such as `prompt/prompt_kernel_v3.5.md` and `meta/prompt_genome.json`.
2. **Event Bus Setup** — Publish and subscribe to the AsyncEventBus channels described in [Agent System Overview](agent_system_overview.md). Typical topics include `campaign.launch`, `analysis.report`, `config.update`, and `heartbeat.check`.
3. **Shared Memory** — Read and write semantic data using the mechanisms in `o3research/core/semantic_cache.py`. Agents should store embeddings or summaries for reuse by others.
4. **PromptOps Workflow** — Route any prompt or configuration changes through the ConfigAgent. CI validation ensures that updates are tracked in `prompt_evolution_log/v3.5.yaml`.

## Recommended Repository Structure
External agents should expect these directories:

```
docs/prompt/          # Prompt kernels and templates
docs/meta/            # Prompt genome, evaluation logs, version diffs
config/               # Runtime settings and environment flags
o3research/agents/    # Reference agent implementations
```

## Example Message Topics
- `campaign.launch`
- `analysis.report`
- `config.update`
- `heartbeat.check`

These topics enable real-time collaboration and monitoring. See [72-Hour Campaign Simulation](simulations/72hr_campaign_sim.md) for a practical workflow example.
