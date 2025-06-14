# Golden Prompts (v4.0.0)

This directory contains reference prompts for validating the O3 Prompt Kernel architecture. These golden prompts serve as test cases to ensure the system behaves as expected across different scenarios.

## Purpose

Golden prompts are used to:
- Validate core functionality
- Ensure backward compatibility
- Test multi-agent coordination
- Verify memory and reflection capabilities
- Test KPI-driven optimization logic

## Included Tests

| File | Purpose | Key Features Tested |
|------|---------|-------------------|
| `test_prompt_coordinator.md` | Validates multi-agent coordination and ReAct patterns | Agent communication; ReAct-style reasoning; Feedback loops |
| `test_memory_reflection.md`  | Tests memory retrieval and meta-reflection capabilities | Memory access; Reflection loops; Performance learning |
| `test_kpi_optimization.md`   | Validates KPI-driven optimization strategies | KPI tracking; Content strategy; Performance optimization |
| `test_config_adjustment.md`  | Tests configuration updates and schema diffs | ConfigAgent validation; Self-reflection |
| `test_config_routing_diff.md` | Validates routing table adjustments | ConfigAgent diff summary; Alert routing |
| `test_config_schema_diff.md` | Validates schema mutations | ConfigAgent schema diff; Compatibility warnings |
| `test_campaign_planning.md` | Generates cross-channel campaign plan | Budget allocation; Multi-channel sequencing |
| `test_summary_by_channel.md` | Summarizes performance metrics by channel | Channel-level KPIs; Quick insights |
| `test_top_segment_budget.md` | Creates budget plan for highest-performing segment | Segment analysis; ROI focus |
| `test_creative_generation.md` | Produces new ad creative examples | Image/copy combos; Brand consistency |
| `test_sandbox_push.md` | Validates sandbox environment push | ConfigAgent sandbox trigger; No production impact |

## Usage

These prompts are automatically validated by the CI pipeline on each commit. To run validation locally:

```bash
# Install dependencies (one time)
./scripts/setup_env.sh

# Run markdown validation
markdownlint-cli2 "tests/golden_prompts/*.md"

# Check for required sections
bash scripts/validate_golden_prompts.sh
```

## Versioning

- **Current Version**: 3.5.10
- **Compatibility**: O3 Prompt Kernel v3.5.0+
- **Last Updated**: 2025-05-30

## Contributing

When adding new golden prompts:
1. Follow the template structure
2. Include all required sections (INPUT, EXPECTED, NOTES)
3. Add relevant tags
4. Update this README
5. Ensure CI passes
## Related Documentation
- [Prompt Kernel v3.5 Documentation](./../../docs/prompt/prompt_kernel_v4.md)
- [Testing Guidelines](../../docs/contribution_guide.md)
- [CI Configuration](./../../.github/workflows/validate_repo.yml)
