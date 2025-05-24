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
- [ChatGPT Research Workflow](docs/chatgpt_research_workflow.md) - Quickstart for using this repo with ChatGPT

### Research & Methodology
- [Research Goals](docs/RESEARCH_GOALS.md) - Overview of research objectives and success metrics
- [Methodology](docs/METHODOLOGY.md) - Detailed research approach and tools

### Project Management
- [Contribution Guide](docs/contribution_guide.md) - How to contribute to the project
- [Release Checklist](docs/meta/release_checklist_v3.5.md) - Process for new releases
- [Changelog](CHANGELOG.md) - Version history and changes

## 📂 Repository Structure (V3.5.3)

```
.
├── .github/                     # GitHub configurations
│   └── workflows/               # CI/CD workflows
│       └── validate_repo.yml    # Repository validation
├── docs/                        # Documentation
│   ├── prompt/                  # Prompt engineering
│   │   ├── prompt_kernel_v3.5.md  # Core prompt (latest)
│   │   └── prompt_kernel_v3.4.md  # Legacy prompt
│   ├── meta/                    # System metadata
│   │   ├── prompt_evolution_log/ # Version history
│   │   │   └── v3.5.yaml       # v3.5 evolution log
│   │   ├── meta_evaluation.json # Evaluation framework
│   │   └── release_checklist_v3.5.md
│   ├── performance_marketing/   # Marketing strategies
│   ├── RESEARCH_GOALS.md        # Research objectives
│   ├── METHODOLOGY.md          # Research methodology
│   └── source_index.json       # Reference index
├── tests/                       # Test specifications
│   └── test_o3_context.json    # Context validation
├── CHANGELOG.md                # Version history
└── README.md                   # Project overview
    │   ├── mckinsey_ai_marketing.md
    │   ├── neurogym_neuromarketing.md
    │   └── reforge_growth_loops.md
    ├── meta/                    # Meta-level documentation
    │   ├── prompt_genome.json   # Prompt lineage and evolution
    │   └── meta_evaluation_template.md  # Evaluation framework
    ├── prompt/                  # Core prompt definitions
    │   ├── prompt_kernel_v3.4.md  # V3.4 Unified Final prompt
    │   └── prompt_kernel_v3.md   # V3.2 (deprecated)
    └── simulations/             # Simulation scenarios
        └── 72hr_campaign_sim.md # 72-hour PPC simulation
```

## 🚀 Quick Start

### For O3 Deep Research V3.4
Reference this repository in your prompts using:

```
📘 EXTERNAL KNOWLEDGE CONTEXT:
Use GitHub repository: https://github.com/DanCanadian/ADK

Key references:
- docs/ADK_quickstart.md
- docs/adk_docs_snapshot.md
- docs/kaggle_prompt_engineering_summary.md
- docs/prompt/prompt_kernel_v3.4.md  # Core V3.4 prompt
- docs/performance_marketing/*.md
- docs/meta/prompt_genome.json  # Version and lineage tracking
- docs/source_index.json
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
# Install dependencies
npm install -g markdownlint-cli2

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
```

## 📚 Repository Structure

```
.
├── docs/                           # Documentation root
│   ├── ADK_quickstart.md           # Google ADK quickstart guide
│   ├── adk_docs_snapshot.md        # Core ADK documentation
│   ├── integration_guide_o3.md     # O3 Deep Research integration
│   ├── kaggle_prompt_engineering_summary.md
│   └── performance_marketing/      # Marketing resources
│       ├── google_insights_summary.md
│       ├── hubspot_ai_automation.md
│       ├── mckinsey_ai_marketing.md
│       ├── meta_ai_strategy.md
│       ├── neurogym_neuromarketing.md
│       ├── reforge_growth_loops.md
│       ├── skai_roi_optimization.md
│       └── smartly_creative_ai.md
├── .gitattributes                  # Git configuration
└── README.md                      # This file
```

## 🔍 Source Index

All sources are indexed in `docs/source_index.json` with tags for easy reference:

- ADK & Architecture
- Prompt Engineering
- Neuromarketing & Growth
- Marketing Automation
- AI Strategy

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
- [Reforge Growth Systems](https://www.reforge.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Google Cloud AI](https://cloud.google.com/ai)
- [Google Cloud Docs](https://cloud.google.com/docs)
- [IBM Developer AI](https://developer.ibm.com/technologies/artificial-intelligence/)
- [IBM AI Learning Path](https://developer.ibm.com/learningpaths/get-started-artificial-intelligence/)
- [IBM Technology YouTube](https://www.youtube.com/@IBMTechnology)

### Prompt Reference
- [O3 Deep Research Prompt](docs/o3_deep_research_prompt.md) — The full V3 instruction set for launching O3 Deep Research analysis.
