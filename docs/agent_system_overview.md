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
└─ tests/
```

_Diagrams from the original 21 May prompt illustrate this layout. See [Prompt Kernel v3.5](prompt/prompt_kernel_v3.5.md) for visuals._

Example skeletons of `BaseAgent` and `ResearchAgent` are provided in the
`src/` directory for reference. These stubs demonstrate the minimal interface
used by more advanced agents.

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
| GovernanceAgent | Compliance monitoring and escalation | Overseer | heartbeat_checker | Policy gate | Alert & retry logic |
| MCPServer | Orchestration layer across agents | Coordinator | mcp_server, routing_table | Routing prompts | Cross-agent feedback |
| GovernanceAgent | Compliance & escalation | Overseer | governance_module | Policy prompts | Heartbeat monitoring |

## Development Pipeline

1. **Design** – Define agent personas, prompt scaffolds and coordination protocols.
2. **Training** – Tune prompts, craft reasoning paths and register the prompt genome.
3. **Evaluation** – Run the test suite and score outputs for clarity, accuracy and cost.
4. **Deployment** – Push validated prompts, register agents and collect feedback for continuous improvement.

## Roadmap Highlights

- **Phase 1: Minimum Viable Agent System (0–3 months)** – Deploy ResearchAgent, ContentAgent and CampaignAgent.
- **Phase 2: Multi-Agent Orchestration (3–6 months)** – Introduce EngagementAgent, OptimizationAgent and AnalyticsAgent with shared memory.
- **Phase 3: Self-Tuning and Scaling (6–12 months)** – Add ConfigAgent and automated prompt evolution across all agents.

> **Diagram Note**: The roadmap and module map were first visualized in the 21 May 2025 prompt kernel. This document condenses those graphics into text for quick reference.

## Inter-Agent Governance

To ensure reliability and compliance, a **GovernanceAgent** oversees critical rules and handles escalation scenarios. This agent monitors heartbeat signals from all active agents and enforces retry policies when failures occur.

### Heartbeat & Retry Logic

1. Each agent emits a heartbeat message via the orchestration bus every five minutes.
2. The GovernanceAgent records these heartbeats and triggers a retry if an expected signal is missed twice.
3. Failed prompts are logged with context so ConfigAgent can analyze schema drift.
