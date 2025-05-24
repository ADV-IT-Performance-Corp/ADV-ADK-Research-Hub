# ChatGPT Research Workflow

This quickstart describes how to work with this repository through the ChatGPT interface to run O3 Deep Research.

1. **Connect the Repository**
   - In ChatGPT, choose **Connect GitHub Repository**.
   - Select `ADK` or paste the repository URL.

2. **Explore Key Files**
   - `README.md` – overview and documentation links.
   - `docs/agent_system_overview.md` – map of agents and modules.
   - `docs/source_index.json` – registry of reference files.

3. **Validate Locally**
   - Run `markdownlint-cli2 "**/*.md" "#node_modules"`.
   - Run `yamllint -d '{extends: default, rules: {line-length: {max: 120, allow-non-breakable-inline-mappings: true}}}' .`
   - Run `jq . docs/source_index.json`.

4. **Reference Materials**
   - For GitHub linking details see [GitHub Integration Guide](docs/github_chatgpt_integration.md).
   - For system architecture see [Agent System Overview](docs/agent_system_overview.md).

Use these steps to quickly spin up a research session and validate changes.
