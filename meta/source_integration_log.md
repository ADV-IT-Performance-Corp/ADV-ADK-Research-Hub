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

## [2025-05-30] External Source Restructure

- Moved documentation stubs into `/docs/external/{prompting,devops,memory,governance,analytics}`
- Added `last_reviewed` metadata for each external source
- Updated `source_index.json` metadata timestamp
- Added scripts for source index generation and offline link checks

Codex Commit: `feat(docs): organize external references`
