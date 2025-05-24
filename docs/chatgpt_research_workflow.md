# ChatGPT Research Workflow Quickstart

This guide explains how to connect the ADK repository to ChatGPT for O3 Deep Research and validate files locally.

## Connect the Repository
1. In ChatGPT, choose **Connect GitHub Repository**.
2. Select the repository `ADK` and authorize access.
3. ChatGPT can now read files and reference them in conversations.

## Local Validation Steps
Run these commands from the repository root to ensure formatting and metadata consistency:

```bash
npx markdownlint-cli2 "docs/**/*.md" '!docs/legacy/**'
yamllint -d '{extends: default, rules: {line-length: {max: 120}}}' .
jq . docs/source_index.json
```

Use file path references in your prompts so ChatGPT can cite specific sections accurately.
