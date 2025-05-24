# ChatGPT Research Workflow Quickstart

This guide shows how to connect this repository to ChatGPT and run validation commands locally.

## Connecting the Repository
1. In ChatGPT, choose **Connect GitHub Repository**.
2. Authorize access to your GitHub account and select the repository `ADK`.
3. After connecting, ChatGPT can read files and cite them during analysis.

## Local Validation
Run these commands from the repository root:

```bash
npm install -g markdownlint-cli2
pip install yamllint jq
npx markdownlint-cli2 "**/*.md" "#node_modules"
yamllint -d '{extends: default, rules: {line-length: {max: 120}}}' .
jq . docs/source_index.json
```

## Next Steps
- Review the [Agent System Overview](agent_system_overview.md) for module roles.
- See the [GitHub Integration Guide](github_chatgpt_integration.md) for additional tips.
