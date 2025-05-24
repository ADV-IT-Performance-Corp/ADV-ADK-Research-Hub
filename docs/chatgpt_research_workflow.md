# ChatGPT Research Workflow Quickstart

This guide explains how to connect your GitHub repository to ChatGPT for O3 Deep Research and run local validations.

## 1. Connect GitHub
1. Open ChatGPT and select **Connect GitHub Repository**.
2. Authorize access to your GitHub account and choose the repository `ADK`.
3. ChatGPT can now read files and reference them during conversations.

## 2. Run Local Validation
Install the required tools and run checks:

```bash
npm install -g markdownlint-cli2
pip install yamllint jq

# Validate markdown
markdownlint-cli2 "docs/**/*.md" '!docs/legacy/**'

# Validate YAML
yamllint -d '{extends: default, rules: {line-length: {max: 120}}}' .

# Check JSON
jq . docs/source_index.json
```

Keeping validations green ensures the repository works smoothly with O3 Deep Research.
