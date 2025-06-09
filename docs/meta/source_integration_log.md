# Source Integration Log

## [2025-05-29] External Source Integration – Prompted by PROMPTFORGE

Integrated the following 24 sources into `/docs/source_index.json` and created `.md` stubs in `/docs/external/`:

- Google Docs API
- LangChain Docs
- OpenAI Cookbook
- Claude API Docs
- A2A Protocol
- n8n Docs
- MCP Server API
- Airtable API
- Vertex AI Grounding
- Amplitude Docs
- Ray Serve Docs
- MLflow
- Weights & Biases Docs
- FastAPI Docs
- Helm Charts (K8s)
- Anthropic Prompting Guide
- DeepMind Gopher Prompt Lab
- FLAN-T5 Prompt Patterns
- CognitiveLoad Design
- TinyML / Edge AI
- Apple ML APIs
- AI Fairness 360 Toolkit
- GDPR Prompting Compliance
- OpenPrompt Evaluator

Codex Commit: `feat(sources): added external documentation references`

## [2025-05-30] External Source Organization

- Moved external stubs into `prompting/`, `devops/`, and `governance/` subfolders
- Added cross links and example code snippets to select stubs
- Introduced `scripts/update_source_index.py` for automatic JSON regeneration
- Created `scripts/offline_link_check.sh` with `docs/link_cache.txt`
- Rebuilt `docs/source_index.json` with `description`, `used_by`, and `last_reviewed` fields

Codex Commit: `feat(docs): organize external sources with automation`
