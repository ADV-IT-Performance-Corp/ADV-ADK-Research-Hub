# Utility Scripts

This folder contains helper scripts used to manage the local development
environment and validate golden prompt files.

- **setup_env.sh** – installs Node.js, `markdownlint-cli2`, `jq`, and `yamllint`
  so that local checks match the CI pipeline.
- **validate_golden_prompts.sh** – verifies that each markdown file in
  `tests/golden_prompts/` contains the required `### INPUT`, `### EXPECTED`, and
  `### NOTES` sections, includes version references, and declares `**Tags:**`.

Run `./setup_env.sh` once to install dependencies and then execute
`bash validate_golden_prompts.sh` whenever you modify the golden prompt tests.
