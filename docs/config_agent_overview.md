# ConfigAgent Overview

The **ConfigAgent** manages prompt settings, routing weights, and schema updates across all agents. It ensures configuration changes are tested and rolled out safely.

## Responsibilities
- Monitor prompt drift and update routing tables
- Validate schema changes against the prompt genome
- Apply A/B tests for new configurations

## Schema Diff Example

```json
{
  "old": {
    "routing_weight": 0.5,
    "tone": "formal"
  },
  "new": {
    "routing_weight": 0.7,
    "tone": "conversational"
  }
}

```

The ConfigAgent compares versions and triggers validation tests before deployment.

## Related Documentation
- [Integration Guide](integration_guide_o3.md)
- [Prompt Kernel v3.5](prompt/prompt_kernel_v3.5.md)
