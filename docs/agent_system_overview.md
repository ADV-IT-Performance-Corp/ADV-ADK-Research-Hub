# Agent System Overview

This overview summarizes the main modules and agent roles defined in the O3 Deep Research repository.

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

## Agent Roles

| Agent | Business Function | ADK Modules | Prompt Type | Feedback Loop |
|-------|------------------|-------------|-------------|---------------|
| ResearchAgent | Market and competitor insights | memory_buffer, scoring_toolkit | Chain-of-Thought | External validation |
| ContentAgent | Blog and ad copy generation | base_agent, few_shot_selector | Instructional few-shot | Self-reflection |
| CampaignAgent | Campaign launch and iteration | orchestration_engine | Planning + loop scoring | Metadata reflection |
| EngagementAgent | Email flows and retargeting | routing_agent, tone_modeler | Motivational adaptive | Reforge loop |
| OptimizationAgent | Ad tuning and ROAS balancing | realtime_feedback, metric_map | Self-calibrating | Metric-weighted loop |
| AnalyticsAgent | Performance tracking | insight_collector, delta_tracker | Reflective analysis | Summary validation |
| ConfigAgent | Prompt and routing tuning | config_mutator, score_aligner | Schema-driven | Prompt genome refinement |

Use this overview as a reference when designing new agents or expanding the system.
