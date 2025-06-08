# O3 Deep Research - AI Marketing Automation System

[![O3 Version](https://img.shields.io/badge/version-3.5.7-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![CI/CD](https://github.com/DanCanadian/ADK/actions/workflows/validate_repo.yml/badge.svg)](https://github.com/DanCanadian/ADK/actions)

This repository powers the O3 Deep Research initiative, an advanced AI-powered marketing automation system for ADV IT Performance Corp. It implements the V3.5 Unified Final prompt architecture with enhanced CI/CD validation, comprehensive research capabilities, and advanced agent coordination.

## 🚀 Key Features (v3.5.7)

- **Enhanced Multi-Agent System**: Specialized agents with clear responsibilities and improved coordination
- **Asynchronous Event Bus**: Async publish/subscribe layer for agent communication
- **Advanced Prompt Patterns**: Implements ReAct, Chain-of-Thought, and Few-shot prompting
- **Self-Improving Architecture**: Built-in feedback loops and memory systems
- **Enterprise-Grade CI/CD**: Automated validation and deployment pipelines
- **Comprehensive Documentation**: Clear guidelines and evolution tracking

## 📚 Documentation

### Core Documentation
- [Prompt Kernel v3.5](docs/prompt/prompt_kernel_v3.5.md) - Core prompt engineering framework (latest)
- [Prompt Evolution Log](docs/meta/prompt_evolution_log/v3.5.yaml) - Version history and changes
- [Meta Evaluation](docs/meta/meta_evaluation.json) - Evaluation framework and metrics
- [Meta Evaluation Usage](docs/meta/meta_evaluation.md) - How to compute weighted scores
- [Evaluation Results](docs/meta/evaluation_results.json) - Scores recorded for each release
- [GitHub Integration Guide](docs/github_chatgpt_integration.md) - Connect this repository to ChatGPT
- [O3 Integration Guide](docs/integration_guide_o3.md) - Setup and orchestration steps
- [AGENTS Guide](AGENTS.md) - Short rules for using ChatGPT with this repo
- [Agent System Overview](docs/agent_system_overview.md) - Module map and agent roles
- [ConfigAgent Overview](docs/config_agent_overview.md) - Prompt configuration management
- [Configuration Settings Reference](docs/config/settings_reference.md) - Details for `settings.yaml`
- [GovernanceAgent Concept](docs/governance_agent_concept.md) - Proposed compliance layer
- [World Agent Integration Blueprint](docs/world_agent_integration.md) - Connect external agents via the event bus
- [Documentation Index](docs/tree.md) - Overview of all docs

### Research & Methodology
- [Research Goals](docs/RESEARCH_GOALS.md) - Overview of research objectives and success metrics
- [Methodology](docs/METHODOLOGY.md) - Detailed research approach and tools

### Project Management
- [Contribution Guide](docs/contribution_guide.md) - How to contribute to the project
- [Release Checklist](docs/meta/release_checklist_v3.5.md) - Process for new releases
- [Changelog](CHANGELOG.md) - Version history and changes

## 📂 Repository Structure (v3.5.7)

```text
.
├── .github/
│   └── workflows/
├── src/
│   ├── core/
│   └── agents/
├── config/
│   └── settings.yaml
├── docs/
│   ├── prompt/
│   ├── meta/
│   ├── performance_marketing/
│   ├── RESEARCH_GOALS.md
│   ├── METHODOLOGY.md
│   └── source_index.json
├── tests/
│   └── golden_prompts/
├── scripts/
├── examples/
│   └── simple_workflow.py
└── README.md
```

## 🚀 Quick Start

### For O3 Deep Research V3.5
Reference this repository in your prompts using:

📘 EXTERNAL KNOWLEDGE CONTEXT:
Use GitHub repository: https://github.com/DanCanadian/ADK

Key references:
- docs/ADK_quickstart.md
- docs/adk_docs_snapshot.md
- docs/kaggle_prompt_engineering_summary.md
- docs/prompt/prompt_kernel_v3.5.md  # Core V3.5 prompt
- docs/performance_marketing/*.md
- docs/meta/prompt_genome.json  # Version and lineage tracking
- docs/source_index.json

Run the demo workflow:

```bash
python examples/simple_workflow.py
```

## 🛠️ CI/CD Validation

This repository includes GitHub Actions workflows that automatically validate:

- Markdown formatting and linting
- JSON syntax validation
- Broken link checking
- Required file presence
- Version consistency
- CHANGELOG format

To run validations locally:

```bash
# Install dependencies (one time)
./scripts/setup_env.sh

# Run markdown linting
markdownlint-cli2 "**/*.md" "#node_modules"

# Check for TODOs and placeholders
grep -r "TODO\|Coming soon\|placeholder" --include="*.md" --include="*.json" --include="*.yml" --include="*.yaml" .
# Rebuild source index and run offline link check
python3 scripts/update_source_index.py
bash scripts/offline_link_check.sh
  python scripts/refresh_link_cache.py
```

- `python scripts/refresh_link_cache.py` refreshes external link status.

Note: The `node_modules/` directory is excluded via `.gitignore` to avoid large diffs. Do not commit this folder.

### For Developers
1. Clone this repository:

   ```bash
   git clone https://github.com/adv-ai/o3-deep-research-context.git
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. The current release version is stored in the `VERSION` file and exposed as
   `src.__version__` for programmatic access.
4. After publishing a release, record the evaluation scores in
   `docs/meta/evaluation_results.json` with the reviewer name and date.

### Pre-commit
Install the pre-commit framework and set up the hooks:

```bash
pip install pre-commit
pre-commit install
```

Running `pre-commit` will execute markdownlint, yamllint, golden prompt validation, and unit tests.

### Running Tests Manually
You can execute the full test suite without the pre-commit hooks:

```bash
python -m pytest
```

This runs the agent and core tests defined in `tests/`.

## 📚 Core References

- [Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart)
- [Prompt Engineering Guide](https://www.kaggle.com/whitepaper-prompt-engineering)
- [Performance Marketing Strategies](/docs/performance_marketing/)

## 🔗 External Sources

See [source_index.json](/docs/source_index.json) for a complete list of referenced external sources including:
- Google Cloud & Vertex AI
- OpenAI Platform
- IBM Developer Resources
- Microsoft AI Builder
- NVIDIA & AMD Developer Hubs
- Reforge Growth Systems
- NeuroGym
External stubs are organized under `docs/external/` by category: `prompting`, `devops`, and `governance`.

```text
EXTERNAL KNOWLEDGE CONTEXT:
Repository: https://github.com/DanCanadian/ADK

Key references:
- docs/ADK_quickstart.md — Official ADK patterns and quickstart
- docs/adk_docs_snapshot.md — Core ADK modules and architecture
- docs/kaggle_prompt_engineering_summary.md — Advanced prompt patterns
- docs/performance_marketing/ — Marketing automation strategies
```

## 🔍 Source Index

All sources are indexed in `docs/source_index.json` with tags for easy reference:

- ADK & Architecture
- Prompt Engineering
- Neuromarketing & Growth
- Marketing Automation
- AI Strategy
External stubs are organized under `docs/external/` by category (prompting, devops, integrations, governance).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 References

### Core References
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Agent Development Kit](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/overview)
- [Kaggle Prompt Engineering Whitepaper](https://www.kaggle.com/whitepaper-prompt-engineering)

### Extended Source Integration
- [Think with Google](https://www.thinkwithgoogle.com/)
- [Meta Ads AI](https://www.facebook.com/business/ads)
- [HubSpot AI](https://blog.hubspot.com/marketing/ai-marketing-strategy)
- [Skai AI Marketing](https://www.skai.io/blog)
- [Smartly Creative AI](https://www.smartly.io/resources)
- [McKinsey AI Insights](https://www.mckinsey.com/featured-insights/artificial-intelligence)
- [NeuroGym](https://www.myneurogym.com/)
External stubs are organized under `docs/external/` by category: `prompting`, `devops`, and `governance`.
- [Reforge Growth Systems](https://www.reforge.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Google Cloud AI](https://cloud.google.com/ai)
- [Google Cloud Docs](https://cloud.google.com/docs)
- [IBM Developer AI](https://developer.ibm.com/technologies/artificial-intelligence/)
- [IBM AI Learning Path](https://developer.ibm.com/learningpaths/get-started-artificial-intelligence/)
- [IBM Technology YouTube](https://www.youtube.com/@IBMTechnology)

### Prompt Reference
- [O3 Deep Research Prompt](docs/o3_deep_research_prompt.md) — The full V3 instruction set for launching O3 Deep Research analysis.
