# ChatGPT Research Workflow Quickstart

This guide explains how to connect this repository to ChatGPT and validate files locally before opening pull requests.

## Connect the Repository
1. Open ChatGPT and select **Connect GitHub Repository**.
2. Authorize your GitHub account and choose `ADK`.
3. Once connected, reference files by their path (e.g., `docs/prompt/prompt_kernel_v3.5.md`).

## Validate Locally
Run the same checks used in CI:

```bash
# Lint Markdown files
markdownlint-cli2 "docs/**/*.md" '!docs/legacy/**'

# Validate YAML
yamllint -d '{extends: default, rules: {line-length: {max: 120, allow-non-breakable-inline-mappings: true}}}' .

# Validate JSON
jq . docs/source_index.json
```

Keep the repository up to date so ChatGPT always reads the latest version.
