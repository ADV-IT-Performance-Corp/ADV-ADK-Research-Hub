# ChatGPT Research Workflow Quickstart

This guide explains how to connect this repository to ChatGPT and validate files locally. Follow these steps after cloning the repo.

## 1. Connect the Repository
- In ChatGPT, choose **Connect GitHub Repository**.
- Authorize access and select `ADK`.
- ChatGPT can now reference files by path, allowing you to cite sources in your prompts.

## 2. Run Local Validations
Before committing changes run:

```bash
npm install -g markdownlint-cli2
markdownlint-cli2 "**/*.md" "#node_modules"
yamllint -d '{extends: default, rules: {line-length: {max: 120, allow-non-breakable-inline-mappings: true}}}' .
jq . docs/source_index.json
```

These steps mirror the CI workflow and help catch formatting errors early.

## 3. Reference Documents by Path
When crafting prompts for O3 Deep Research, cite files using relative paths. Example:

```text
Use information from docs/performance_marketing/google_insights_summary.md
```

See [github_chatgpt_integration.md](github_chatgpt_integration.md) for troubleshooting connection issues.
