# ConfigAgent Overview

The **ConfigAgent** manages prompt configuration and routing rules across the O3 agent ecosystem. It monitors schema drift, applies updates, and triggers test cases to ensure stable operation.

## Example Schema Diff

```yaml
# v3.5.2
routing:
  research: research_agent_v1
  content: content_agent_v1
# v3.5.3
routing:
  research: research_agent_v1
  content: content_agent_v2  # updated tone model
```

## Test Cases
1. Validate that new routing schemas parse correctly using `yaml.safe_load`.
2. Ensure backward compatibility by running golden prompts against the previous configuration.
3. Trigger ConfigAgent's self-reflection loop when a schema diff introduces errors.

For more context on integration, see [integration_guide_o3.md](integration_guide_o3.md).
