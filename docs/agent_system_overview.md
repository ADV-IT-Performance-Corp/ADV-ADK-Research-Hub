# Agent System Overview

This document summarizes the core modules, agent roles, and development lifecycle for the O3 Deep Research marketing automation system.
For setup instructions see the [Integration Guide](integration_guide_o3.md).

## Module Map

```
o3research/
├── core/
│   ├── semantic_cache.py
│   ├── few_shot_selector.py
│   ├── token_optimizer.py
│   └── self_reflection.py
├── flows/
│   ├── marketing_flow.yaml
│   └── strategy_flow.yaml
├── agents/
│   ├── research_agent.py
│   ├── content_agent.py
│   ├── campaign_agent.py
│   ├── engagement_agent.py
│   ├── optimization_agent.py
│   ├── analytics_agent.py
│   ├── config_agent.py
│   └── mcp_server.py
├── utils/
│   ├── api_clients/
│   ├── data_processors/
│   └── monitoring/
config/
│   ├── settings.yaml
│   └── prompts/
tests/
```

_Diagrams from the original 21 May prompt illustrate this layout. See [Prompt Kernel v3.5](prompt/prompt_kernel_v3.5.md) for visuals._

Example skeletons of `google.adk.Agent` and `ResearchAgent` are provided in the
`o3research/` directory for reference. These stubs demonstrate the minimal interface
used by more advanced agents.

## Event Bus

Agents communicate through a lightweight publish/subscribe layer. Version 3.5.7
introduces an **AsyncEventBus** using Python's `asyncio` so agents can handle
messages concurrently while logging activity for easier debugging.

Example usage is shown in [examples/simple_workflow.py](../examples/simple_workflow.py)
which runs `flows/marketing_flow.yaml` locally:

```python
from google.adk.runners import InMemoryRunner

runner = InMemoryRunner(flow="flows/marketing_flow.yaml")
runner.run()
```

## Agent Functional Mapping

| Agent | Business Function | LLM Role | ADK Modules | Prompt Type | Feedback Loop Type |
|-------|------------------|---------|-------------|-------------|--------------------|
| ResearchAgent | Competitor intel, trend scan | Synthesizer | memory_buffer, scoring_toolkit | Chain-of-Thought | External + semantic validation |
| ContentAgent | Blog generation for PPC | Generator | few_shot_selector | Instructional few-shot | Self-reflection with score |
| CampaignAgent | Campaign launch and iteration | Planner | orchestration_engine | Planning loop | Loop-based metadata reflection |
| EngagementAgent | Email flows, retargeting | Motivator | routing_agent, tone_modeler | Motivational adaptive | Reforge loop scoring |
| OptimizationAgent | Ad tuning and performance balancing | Calibrator | realtime_feedback, metric_map | Self-calibrating prompt | Metric-weighted ROAS tuning |
| AnalyticsAgent | Performance tracking and reporting | Interpreter | insight_collector, delta_tracker | Reflective analysis | Periodic summary validation |
| GovernanceAgent | Compliance monitoring & escalation | Overseer | heartbeat_monitor | Policy prompts | Alert & retry logic |
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

## Diagrams
The 21 May prompt introduced a sequential flow diagram showing Research →
Content → Campaign → Optimization → Analytics. See the
[prompt kernel](prompt/prompt_kernel_v3.5.md#module-map) for visuals.

A simplified textual view of the agent handoff looks like:

```
ResearchAgent
   ↓
ContentAgent
   ↓
CampaignAgent
   ↓
OptimizationAgent
   ↓
AnalyticsAgent
   ↺ (insights loop back to ResearchAgent)
```

For connection instructions refer to the
[Integration Guide](integration_guide_o3.md).
