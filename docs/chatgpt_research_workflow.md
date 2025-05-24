# ChatGPT Research Workflow Quickstart

This quickstart explains how to connect ChatGPT to this repository and validate files locally.

## Connect the Repository

1. In ChatGPT, click **Connect GitHub Repository**.
2. Select your GitHub account and choose the repository `ADK`.
3. Authorize access so ChatGPT can read the files.

After connecting, reference documents by path to get accurate citations.

## Local Validation Commands

Install the required tools:

```bash
npm install -g markdownlint-cli2
pip install yamllint jq
```

Run validations from the repository root:

```bash
npx markdownlint-cli2 "**/*.md" "#node_modules"
yamllint -d '{extends: default, rules: {line-length: {max: 120}}}' .
jq . docs/source_index.json
```

These checks match the CI workflow and should pass before opening a pull request.
