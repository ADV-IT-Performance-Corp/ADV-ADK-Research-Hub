# Agent System Overview

This document provides a high-level summary of how the O3 Deep Research agents are organized within the repository. It outlines the core modules, each agent's role, and the feedback loops that tie them together.

## Module Map

```
agent_system_adk/
├── src/
│   ├── core/
│   │   ├── base_agent.py
│   │   ├── semantic_cache.py
│   │   ├── few_shot_selector.py
│   │   ├── token_optimizer.py
│   │   └── self_reflection.py
│   ├── agents/
│   │   ├── research_agent.py
│   │   ├── content_agent.py
│   │   ├── campaign_agent.py
│   │   ├── engagement_agent.py
│   │   ├── optimization_agent.py
│   │   ├── analytics_agent.py
│   │   └── config_agent.py
│   └── utils/
│       ├── api_clients/
│       ├── data_processors/
│       └── monitoring/
├── config/
│   ├── settings.yaml
│   └── prompts/
└── tests/
```

## Core Agent Roles

| Agent | Business Function | Feedback Loop |
|-------|------------------|---------------|
| **ResearchAgent** | Competitor intel, trend scan | External validation |
| **ContentAgent** | Blog generation for PPC | Self-reflection |
| **CampaignAgent** | Campaign launch + iteration | Loop-based scoring |
| **EngagementAgent** | Email flows, retargeting | Reforge feedback |
| **OptimizationAgent** | Ad tuning + performance balancing | Metric-weighted ROAS tuning |
| **AnalyticsAgent** | Performance tracking & reporting | Periodic summary validation |
| **ConfigAgent** | Prompt config & routing tuning | Prompt genome refinement |

This overview helps align development and research efforts across the multi-agent system.
