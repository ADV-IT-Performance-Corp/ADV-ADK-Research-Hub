# Google ADK Core Documentation Snapshot

Reference: https://google.github.io/adk-docs/

## ADK Modules Summary

### Core
- `base_agent.py`: interface for all agents
- `semantic_cache.py`: handles cache retrieval and reuse
- `token_optimizer.py`: optimizes token usage
- `few_shot_selector.py`: logic to pick few-shot examples
- `self_reflection.py`: assesses response quality and flags issues

### Agents
- `research_agent.py`
- `content_agent.py`
- `campaign_agent.py`
- `engagement_agent.py`

### Utils
- API clients (integration points)
- Data processors (structured input cleaning)
- Monitoring tools (log + eval)

This ADK structure supports the development of coordinated, reflective, and memory-efficient agents.
