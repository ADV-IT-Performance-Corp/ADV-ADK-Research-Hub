# ConfigAgent Overview

The **ConfigAgent** manages prompt configuration updates and routing logic across all agents. It ensures that prompt schemas remain consistent and allows for controlled experimentation.

## Key Responsibilities
- Maintain the prompt genome and track schema changes
- Apply configuration diffs to agent prompts
- Validate updates with test suites and golden prompts
- Notify other agents via `config_push` messages

## Example Schema Diff

```yaml
before:
  prompt_version: 3.5.7
  routing_weight: 1
after:
  prompt_version: 3.5.7
  routing_weight: 2
```

This diff indicates a version bump and routing change which must pass `validate_golden_prompts.sh` before rollout.
