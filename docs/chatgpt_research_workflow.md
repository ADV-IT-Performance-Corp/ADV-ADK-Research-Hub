# ChatGPT Research Workflow Quickstart

This guide shows how to connect this repository to ChatGPT and validate files locally.

## Connect the Repository
1. Open ChatGPT and choose **Connect GitHub Repository**.
2. Authorize your GitHub account and select the `ADK` repository.
3. ChatGPT can now read files and provide inline citations during research.

## Validate Documentation Locally
Run the following commands from the repository root:

```bash
# Markdown and YAML checks
markdownlint-cli2 "**/*.md" "#node_modules"
yamllint -d '{extends: default, rules: {line-length: {max: 120}}}' .

# Verify the source index
jq . docs/source_index.json
```

These steps mirror the CI workflow so you can ensure the docs are clean before pushing changes.
