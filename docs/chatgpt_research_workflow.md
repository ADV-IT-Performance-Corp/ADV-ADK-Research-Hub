# ChatGPT Research Workflow

This quickstart explains how to leverage ChatGPT with the O3 Deep Research repository.

## 1. Connect the Repository
Follow the [GitHub Integration Guide](github_chatgpt_integration.md) to link the `ADK` repository to ChatGPT.

## 2. Ask Research Questions
Once connected, you can reference repository files directly in your prompts. Example:

```
Refer to the prompt kernel in docs/prompt/prompt_kernel_v3.5.md and summarize the agent roles.
```

## 3. Validate Locally
Before pushing updates, run the repository checks:

```bash
markdownlint-cli2 "**/*.md" "#node_modules"
yamllint -d '{extends: default, rules: {line-length: {max: 120, allow-non-breakable-inline-mappings: true}}}' .
jq . docs/source_index.json
```

These commands ensure documentation and metadata remain consistent.
