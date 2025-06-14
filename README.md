# O3 Deep Research - AI Marketing Automation System

[![O3 Version](https://img.shields.io/badge/version-4.0.0-blue)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![CI/CD](https://img.shields.io/github/actions/workflow/status/ADV-IT-Performance-Corp/ADV-ADK-Research-Hub/validate_repo.yml?branch=master)
![Coverage](coverage.svg)
This repo is built on Google ADK 1.3 + Vertex AI; all agents communicate via the Google Agent‐to‐Agent protocol (A2A v0.6).

This repository powers the O3 Deep Research initiative, an advanced AI-powered marketing automation system for ADV IT Performance Corp. It implements the V3.5 Unified Final prompt architecture with enhanced CI/CD validation, comprehensive research capabilities, and advanced agent coordination.

> **Quick Start**
> - [Google ADK docs](https://google.github.io/adk-docs/)
> - [Vertex AI ADK quick-start](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart)
> - [ADK Python repo](https://github.com/google/adk-python)
> - [gcloud CLI install](https://cloud.google.com/sdk)
> Requires **Python 3.11**.

## 🚀 Key Features (v4.0.0)

- **Enhanced Multi-Agent System**: Specialized agents with clear responsibilities and improved coordination
- **Asynchronous Event Bus**: Async publish/subscribe layer for agent communication
- **Advanced Prompt Patterns**: Implements ReAct, Chain-of-Thought, and Few-shot prompting
- **Self-Improving Architecture**: Built-in feedback loops and memory systems
- **Enterprise-Grade CI/CD**: Automated validation and deployment pipelines
- **Comprehensive Documentation**: Clear guidelines and evolution tracking

## 📚 Documentation

### Core Documentation
- [Prompt Kernel v4](docs/prompt/prompt_kernel_v4.md) - Core prompt engineering framework (latest)
- [Prompt Evolution Log](docs/meta/prompt_evolution_log/v4.yaml) - Version history and changes
- [Meta Evaluation](docs/meta/meta_evaluation.json) - Evaluation framework and metrics
- [Meta Evaluation Usage](docs/meta/meta_evaluation.md) - How to compute weighted scores
- [Evaluation Results](docs/meta/evaluation_results.json) - Scores recorded for each release
- [GitHub Integration Guide](docs/github_chatgpt_integration.md) - Connect this repository to ChatGPT
- [O3 Integration Guide](docs/integration_guide_o3.md) - Setup and orchestration steps
- [AGENTS Guide](AGENTS.md) - Short rules for using ChatGPT with this repo
- [Agent System Overview](docs/agent_system_overview.md) - Module map and agent roles
- [ConfigAgent Overview](docs/config_agent_overview.md) - Prompt configuration management
- [Multi-Client Workflow Runner](docs/orchestration/multi_client.md) - Execute workflows for multiple clients
- [Configuration Settings Reference](docs/config/settings_reference.md) - Details for `settings.yaml`
- [GovernanceAgent Concept](docs/governance_agent_concept.md) - Proposed compliance layer
- [World Agent Integration Blueprint](docs/world_agent_integration.md) - Connect external agents via the event bus
- [Phase 4 Blueprint](docs/Phase_4_Blueprint.md) - Runtime fixes and A2A integration
- [Documentation Index](docs/tree.md) - Overview of all docs
- [Performance Marketing Assistant Architecture](docs/performance_marketing/assistant_architecture.md)
- [Marketing API Integration](docs/performance_marketing/api_integration.md)
- [Prompt Usage Examples](docs/performance_marketing/prompt_usage_examples.md)
- [Marketing Assistant Clients](marketing_assistant/README.md) - Google Ads and GA client usage

### Research & Methodology
- [Research Goals](docs/RESEARCH_GOALS.md) - Overview of research objectives and success metrics
- [Methodology](docs/METHODOLOGY.md) - Detailed research approach and tools

### Project Management
- [Contribution Guide](docs/contribution_guide.md) - How to contribute to the project
  (see checklist; CI fails if the online link check reports errors)
- [Release Checklist](docs/meta/release_checklist_v4.0.md) - Process for new releases
- [Changelog](CHANGELOG.md) - Version history and changes
- [Backup and Restore Guide](docs/operations/backup_and_restore.md) - Recover the repository from nightly backups
- [Version Diff v3.5.7 to v3.5.8](docs/meta/version_diff_v3.5.7_to_v3.5.8.md) - Summary of new modules and docs

## 📂 Repository Structure (v4.0.0)

```text
.
├── .github/
│   └── workflows/
├── o3research/
│   ├── core/
│   └── agents/
├── config/
│   └── settings.yaml
├── docs/
│   ├── prompt/
│   ├── meta/
│   │   └── source_integration_log.md
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

### For O3 Deep Research V4
Reference this repository in your prompts using:

📘 EXTERNAL KNOWLEDGE CONTEXT:
Use GitHub repository: `https://github.com/ADV-IT-Performance-Corp/ADV-ADK-Research-Hub/`

Key references:
- docs/ADK_quickstart.md
- docs/adk_docs_snapshot.md
- docs/kaggle_prompt_engineering_summary.md
- docs/prompt/prompt_kernel_v4.md  # Core V4 prompt
- docs/performance_marketing/*.md
- docs/meta/prompt_genome.json  # Version and lineage tracking
- docs/source_index.json

Run the demo workflows:

```bash
python examples/simple_workflow.py
python examples/marketing_workflow.py
```

### Terminal Setup
Before running any commands, source `shell_config.sh` to load helper aliases. The script also truncates command output to the 1600-byte CI limit.

### Run the Assistant Script

Execute a single end-to-end run with:

```bash
python assistant.py
```

The script prints a campaign summary after completing the workflow.

### Importing Google ADK agents

All marketing modules inherit from `google.adk.Agent`. Import the base class and
ADK runners when extending or testing agents:

```python
from google.adk import Agent
from google.adk.runners import InMemoryRunner

from o3research.marketing import CampaignAgent

class DemoAgent(Agent):
    def run(self, product: str) -> str:
        helper = CampaignAgent()
        return helper.run(product)

agent = DemoAgent(name="demo")
runner = InMemoryRunner(agent)
```

The ADK flow in [flows/marketing_flow.yaml](flows/marketing_flow.yaml) executes
`CampaignAgent`, `BudgetAllocatorAgent`, `EngagementAgent`, and `AnalyticsAgent`
sequentially to automate campaign planning on Vertex AI.

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
npm ci --omit=optional
# Installs Node.js 18.x if missing
# Note: running the script deletes any npm proxy configuration. Export
# required system proxy variables afterwards if needed.

# Run markdown linting
markdownlint-cli2 "docs/**/*.md" "!docs/legacy/**"

# Check docs for TODOs and placeholders
bash scripts/check_incomplete_work.sh
# Rebuild source index and run online link check
python3 scripts/update_source_index.py
# run link check (fails on dead links)
bash scripts/online_link_check.sh
```

Note: The `node_modules/` directory is excluded via `.gitignore` to avoid large diffs. Do not commit this folder.
All helper scripts pipe their output through `head -c 1600` so CI logs remain concise.
CI also checks that no individual line of output exceeds **1600 bytes**. Keep
documentation and command logs under this limit or the workflow will fail.

## Deploying on Vertex AI
See [docs/vertex_ai_quickstart.md](docs/vertex_ai_quickstart.md) for setup steps and
sample code. The guide demonstrates launching
`flows/marketing_flow.yaml` with the Google ADK.

* Example config: `config/vertex_ai.yaml`
* Environment variables sample: `config/vertex_config.yaml`

### Launching Campaigns with Vertex AI
1. Export `VERTEX_PROJECT_ID`, `VERTEX_CREDENTIALS`, and `VERTEX_REGION`.
2. Run:

```bash
python examples/vertex_workflow.py
```

### Using Codex CLI
Run `codex run` to execute workflows locally or in CI.
### Link Validation
Run `bash scripts/online_link_check.sh` to verify external sources are reachable. The command exits with an error if any link is dead.
### For Developers
1. Clone this repository:

   ```bash
   git clone https://github.com/ADV-IT-Performance-Corp/ADV-ADK-Research-Hub.git
   ```

2. Ensure **Python&nbsp;3.11** is installed.

3. Install Python dependencies and the package in editable mode:

   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. Source the provided shell configuration to enable consistent aliases and
   terminal settings:

   ```bash
   source shell_config.sh
   ```

   The script disables colored `grep`, limits `find` output to the first
   200 characters, and resets the terminal width so lines stay within the
   1600-byte CI limit.
5. The current release version is stored in the `VERSION` file and exposed as
   `o3research.__version__` for programmatic access.
6. After publishing a release, record the evaluation scores in
   `docs/meta/evaluation_results.json` with the reviewer name and date.

### Running Tests Manually
You can execute the full test suite using pytest:

```bash
python -m pytest
```

This runs the agent and core tests defined in `tests/`.

### Docker Usage
You can build a lightweight container image using the provided `Dockerfile`:

```bash
docker build -t o3research .
docker run --rm o3research
```

The image installs the Python and Node.js dependencies and runs
`examples/simple_workflow.py` by default. Node.js 18.x is installed during
the build. Mount your own code or override the command to run different
workflows.

## 📚 Core References

- [Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart)
- [Prompt Engineering Guide](https://www.kaggle.com/whitepaper-prompt-engineering)
- [Performance Marketing Strategies](docs/performance_marketing/)
- [Performance Marketing README](docs/performance_marketing/README.md)

## 🔗 External Sources

See [source_index.json](docs/source_index.json) for a complete list of referenced external sources including:
- Google Cloud & Vertex AI
- OpenAI Platform
- IBM Developer Resources
- Microsoft AI Builder
- NVIDIA & AMD Developer Hubs
- Reforge Growth Systems
- NeuroGym
External stubs are organized under `docs/external/` by category: `prompting`, `devops`, and `governance`. A short list of common external docs is available in [docs/refs.md](docs/refs.md).

```text
EXTERNAL KNOWLEDGE CONTEXT:
Repository: `https://github.com/ADV-IT-Performance-Corp/ADV-ADK-Research-Hub/`

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
3. Commit your changes using the conventional prefixes (`feat:`, `fix:`, `chore:`, etc.)
   so CI validates your commit messages
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 References

### Core References
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- Vertex AI Agent Development Kit documentation
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
