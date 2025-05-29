# Utility Scripts

This directory contains helper scripts for local development.

- `setup_env.sh` installs markdownlint, jq, and yamllint so you can run checks locally.

  ```bash
  ./scripts/setup_env.sh
  ```

- `validate_golden_prompts.sh` validates the golden prompt files.

  ```bash
  bash scripts/validate_golden_prompts.sh
  ```

These steps mirror the CI pipeline to help ensure consistency.
