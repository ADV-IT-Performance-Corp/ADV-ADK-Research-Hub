# Agent System Overview

This document summarizes the core modules, agent roles, and development lifecycle for the O3 Deep Research marketing automation system.

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
│   │   ├── config_agent.py
│   │   └── mcp_server.py
│   └── utils/
│       ├── api_clients/
│       ├── data_processors/
│       └── monitoring/
├── config/
│   ├── settings.yaml
│   └── prompts/
└── tests/
```

## Agent Functional Mapping

| Agent | Business Function | LLM Role | ADK Modules | Prompt Type | Feedback Loop Type |
|-------|------------------|---------|-------------|-------------|--------------------|
| ResearchAgent | Competitor intel, trend scan | Synthesizer | memory_buffer, scoring_toolkit | Chain-of-Thought | External + semantic validation |
| ContentAgent | Blog generation for PPC | Generator | base_agent, few_shot_selector | Instructional few-shot | Self-reflection with score |
| CampaignAgent | Campaign launch and iteration | Planner | orchestration_engine | Planning loop | Loop-based metadata reflection |
| EngagementAgent | Email flows, retargeting | Motivator | routing_agent, tone_modeler | Motivational adaptive | Reforge loop scoring |
| OptimizationAgent | Ad tuning and performance balancing | Calibrator | realtime_feedback, metric_map | Self-calibrating prompt | Metric-weighted ROAS tuning |
| AnalyticsAgent | Performance tracking and reporting | Interpreter | insight_collector, delta_tracker | Reflective analysis | Periodic summary validation |
| ConfigAgent | Prompt config and routing tuning | Adjuster | config_mutator, score_aligner | Schema-driven modifiers | Prompt genome refinement |
| MCPServer | Orchestration layer across agents | Coordinator | mcp_server, routing_table | Routing prompts | Cross-agent feedback |

## Development Pipeline

1. **Design** – Define agent personas, prompt scaffolds and coordination protocols.
2. **Training** – Tune prompts, craft reasoning paths and register the prompt genome.
3. **Evaluation** – Run the test suite and score outputs for clarity, accuracy and cost.
4. **Deployment** – Push validated prompts, register agents and collect feedback for continuous improvement.

## Roadmap Highlights

- **Phase 1: Minimum Viable Agent System (0–3 months)** – Deploy ResearchAgent, ContentAgent and CampaignAgent.
- **Phase 2: Multi-Agent Orchestration (3–6 months)** – Introduce EngagementAgent, OptimizationAgent and AnalyticsAgent with shared memory.
- **Phase 3: Self-Tuning and Scaling (6–12 months)** – Add ConfigAgent and automated prompt evolution across all agents.
