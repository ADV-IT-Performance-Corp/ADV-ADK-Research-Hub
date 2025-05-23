# Golden Prompts (v3.5.0)

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
| `test_prompt_coordinator.md` | Validates multi-agent coordination and ReAct patterns | - Agent communication<br>- ReAct-style reasoning<br>- Feedback loops |
| `test_memory_reflection.md`  | Tests memory retrieval and meta-reflection capabilities | - Memory access<br>- Reflection loops<br>- Performance learning |
| `test_kpi_optimization.md`   | Validates KPI-driven optimization strategies | - KPI tracking<br>- Content strategy<br>- Performance optimization |

## Usage

These prompts are automatically validated by the CI pipeline on each commit. To run validation locally:

```bash
# Run markdown validation
markdownlint-cli2 "tests/golden_prompts/*.md"

# Check for required sections
./scripts/validate_golden_prompts.sh
```

## Versioning

- **Current Version**: 3.5.0
- **Compatibility**: O3 Prompt Kernel v3.5.0+
- **Last Updated**: 2025-05-22

## Contributing

When adding new golden prompts:
1. Follow the template structure
2. Include all required sections (INPUT, EXPECTED, NOTES)
3. Add relevant tags
4. Update this README
5. Ensure CI passes

## Related Documentation

- [Prompt Kernel v3.5 Documentation](./../../docs/prompt/prompt_kernel_v3.5.md)
- [Testing Guidelines](./../../docs/TESTING.md)
- [CI Configuration](./../../.github/workflows/validate_repo.yml)
