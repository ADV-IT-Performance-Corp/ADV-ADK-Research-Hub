# Utility Scripts

This folder contains helper scripts for local validation.

## setup_env.sh
Installs Node.js tools and utilities used by CI:

```bash
./scripts/setup_env.sh
```

This installs `markdownlint-cli2`, `jq`, and `yamllint` so you can run repository checks locally.

## validate_golden_prompts.sh
Validates the markdown files in `tests/golden_prompts/`:

```bash
bash scripts/validate_golden_prompts.sh
```

The script verifies each test prompt contains `### INPUT`, `### EXPECTED`, and `### NOTES` sections and that a `**Tags:**` line is present.
