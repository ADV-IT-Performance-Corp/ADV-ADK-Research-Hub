# O3 Deep Research - AI Marketing Automation System

[![O3 Version](https://img.shields.io/badge/version-3.5.3-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![CI/CD](https://github.com/DanCanadian/ADK/actions/workflows/validate_repo.yml/badge.svg)](https://github.com/DanCanadian/ADK/actions)

This repository powers the O3 Deep Research initiative, an advanced AI-powered marketing automation system for ADV IT Performance Corp. It implements the V3.5 Unified Final prompt architecture with enhanced CI/CD validation, comprehensive research capabilities, and advanced agent coordination.

## 🚀 Key Features (v3.5.3)

- **Enhanced Multi-Agent System**: Specialized agents with clear responsibilities and improved coordination
- **Advanced Prompt Patterns**: Implements ReAct, Chain-of-Thought, and Few-shot prompting
- **Self-Improving Architecture**: Built-in feedback loops and memory systems
- **Enterprise-Grade CI/CD**: Automated validation and deployment pipelines
- **Comprehensive Documentation**: Clear guidelines and evolution tracking

## 📚 Documentation

### Core Documentation
- [Prompt Kernel v3.5](docs/prompt/prompt_kernel_v3.5.md) - Core prompt engineering framework (latest)
- [Prompt Evolution Log](docs/meta/prompt_evolution_log/v3.5.yaml) - Version history and changes
- [Meta Evaluation](docs/meta/meta_evaluation.json) - Evaluation framework and metrics
- [GitHub Integration Guide](docs/github_chatgpt_integration.md) - Connect this repository to ChatGPT
- [AGENTS Guide](AGENTS.md) - Short rules for using ChatGPT with this repo
- [Agent System Overview](docs/agent_system_overview.md) - Module map and agent roles
- [Documentation Index](docs/tree.md) - Overview of all docs

### Research & Methodology
- [Research Goals](docs/RESEARCH_GOALS.md) - Overview of research objectives and success metrics
- [Methodology](docs/METHODOLOGY.md) - Detailed research approach and tools

### Project Management
- [Contribution Guide](docs/contribution_guide.md) - How to contribute to the project
- [Release Checklist](docs/meta/release_checklist_v3.5.md) - Process for new releases
- [Changelog](CHANGELOG.md) - Version history and changes


## 📂 Repository Structure (v3.5.3)
├── .github/               # GitHub configuration and workflows
│   └── workflows/
├── docs/                  # Project documentation
│   ├── prompt/            # Prompt engineering docs
│   ├── meta/              # Metadata and release notes
│   ├── performance_marketing/
│   ├── RESEARCH_GOALS.md
│   ├── METHODOLOGY.md
│   └── source_index.json
├── tests/                 # Test specifications
│   └── golden_prompts/    # Prompt validation cases
├── AGENTS.md              # ChatGPT usage rules
├── CHANGELOG.md           # Version history
└── README.md              # Project overview


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

# Check for TODOs
grep -r "TODO\|Coming soon" --include="*.md" --include="*.json" --include="*.yml" --include="*.yaml" .
```

### For Developers
1. Clone this repository:
   ```bash
   git clone https://github.com/adv-ai/o3-deep-research-context.git
   ```

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

```text
EXTERNAL KNOWLEDGE CONTEXT:
Repository: https://github.com/DanCanadian/ADK

Key references:
- docs/ADK_quickstart.md — Official ADK patterns and quickstart
- docs/adk_docs_snapshot.md — Core ADK modules and architecture
- docs/kaggle_prompt_engineering_summary.md — Advanced prompt patterns
- docs/performance_marketing/ — Marketing automation strategies
