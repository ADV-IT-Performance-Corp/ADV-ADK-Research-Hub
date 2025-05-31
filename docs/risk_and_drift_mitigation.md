# Risk and Drift Mitigation Guide

This guide summarizes strategies to reduce prompt drift and manage operational risks for the ADK system.

## Prompt Drift Controls
- **Prompt Genome Tracking**: All prompt changes are versioned in `docs/meta/prompt_genome.json`.
- **Golden Prompt Tests**: `scripts/validate_golden_prompts.sh` validates responses to key prompts.
- **ConfigAgent Rollbacks**: ConfigAgent can revert to a previous prompt version if metrics degrade.

## Operational Resilience
- **Heartbeat Monitoring**: GovernanceAgent checks agent health via the async event bus.
- **Retry & Escalation**: Unresponsive agents trigger retries and escalate to strategists.
- **Persistent Memory**: Critical knowledge is stored in a file-backed memory to survive restarts.

Refer to [governance_agent_overview.md](governance_agent_overview.md) for implementation details.
