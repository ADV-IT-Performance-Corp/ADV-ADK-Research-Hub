# ChatGPT Research Workflow Quickstart

This quickstart explains how to connect the `ADK` repository to ChatGPT, validate changes locally, and cite files in your prompts.

## 1. Connect the Repository
1. Open ChatGPT and choose **Connect GitHub Repository**.
2. Authorize access to your GitHub account and select `DanCanadian/ADK`.
3. ChatGPT can now read repository files during conversations.

## 2. Validate Locally
Run the same checks that CI uses:

```bash
# Markdown linting
npx markdownlint-cli2 "**/*.md" "#node_modules"

# YAML linting
yamllint -d '{extends: default, rules: {line-length: {max: 120}}}' .

# JSON syntax check
jq . docs/source_index.json > /dev/null
```

## 3. Reference Files
When asking ChatGPT about repository content, reference file paths like `docs/prompt/prompt_kernel_v3.5.md` to get precise citations.

Use this workflow as a baseline when exploring the repository with ChatGPT for O3 Deep Research.
