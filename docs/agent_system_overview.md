# Agent System Overview

This document outlines the main modules and agent roles used in the O3 Deep Research project. It acts as a quick reference for new contributors.

## Module Map

```
agent_system_adk/
├── src/
│   ├── core/
│   ├── agents/
│   └── utils/
├── config/
└── tests/
```

## Agent Roles

| Agent | Description | Key Modules |
|-------|-------------|-------------|
| ResearchAgent | Gathers market insights and competitor data | `research_agent.py`, `semantic_cache.py` |
| ContentAgent | Generates multi-format content for campaigns | `content_agent.py`, `few_shot_selector.py` |
| CampaignAgent | Plans and launches PPC campaigns | `campaign_agent.py`, `orchestration_engine` |
| EngagementAgent | Handles email flows and retargeting | `engagement_agent.py`, `tone_modeler` |
| OptimizationAgent | Tunes campaigns for ROAS and budget | `optimization_agent.py`, `realtime_feedback` |
| AnalyticsAgent | Reports performance metrics | `analytics_agent.py`, `delta_tracker` |
| ConfigAgent | Adjusts prompt settings and routing | `config_agent.py`, `config_mutator` |

Each agent communicates through a lightweight messaging bus and shares context via the semantic cache and memory modules.
