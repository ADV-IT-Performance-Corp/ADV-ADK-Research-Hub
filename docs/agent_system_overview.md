# Agent System Overview

This document summarizes the modules and agent roles used in the O3 Deep Research system.

## Module Map
- **core/** – foundational utilities such as `base_agent.py`, `semantic_cache.py`, and `token_optimizer.py`.
- **agents/** – individual agent implementations (research, content, campaign, engagement, optimization, analytics, config).
- **utils/** – helper libraries for API clients, data processing, and monitoring hooks.

## Agent Roles
| Agent | Business Function | Key Modules |
|-------|------------------|-------------|
| ResearchAgent | Market trend scanning and competitor mapping | `memory_buffer`, `scoring_toolkit` |
| ContentAgent | Generates blogs, ads, and social posts | `few_shot_selector`, `tone_modeler` |
| CampaignAgent | Launches and iterates campaigns | `orchestration_engine` |
| EngagementAgent | Handles email flows and retargeting | `routing_agent` |
| OptimizationAgent | Tunes campaigns and budget allocation | `realtime_feedback` |
| AnalyticsAgent | Aggregates performance data | `insight_collector` |
| ConfigAgent | Adjusts prompt settings and routing | `config_mutator` |

These roles collaborate through a messaging bus and share a semantic memory layer for consistent context across the system.
