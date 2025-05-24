# Agent System Overview

This document summarizes the main modules and agent roles implemented in the ADK research framework.

## Module Map

| Path | Purpose |
|------|---------|
| `src/core/` | Base agent classes, semantic cache, token optimizer |
| `src/agents/` | Specialized agents such as `research_agent.py` and `campaign_agent.py` |
| `src/utils/` | API clients, data processors, monitoring tools |
| `config/prompts/` | Prompt templates used across agents |

## Agent Roles

| Agent | Business Function | Key Modules |
|-------|------------------|-------------|
| **ResearchAgent** | Market intelligence and competitor scanning | `memory_buffer`, `scoring_toolkit` |
| **ContentAgent** | Blog and ad copy generation | `few_shot_selector`, `tone_modeler` |
| **CampaignAgent** | Campaign launch and scheduling | `orchestration_engine` |
| **EngagementAgent** | Email flows and retargeting | `routing_agent`, `tone_modeler` |
| **OptimizationAgent** | Budget tuning and ROAS balancing | `realtime_feedback`, `metric_map` |
| **AnalyticsAgent** | Performance tracking | `insight_collector`, `delta_tracker` |
| **ConfigAgent** | Prompt configuration and tuning | `config_mutator`, `score_aligner` |

Agents communicate through a lightweight messaging bus and share context via the semantic cache. Feedback loops allow each agent to refine outputs over time.
