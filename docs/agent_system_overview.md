# Agent System Overview

This document summarizes the O3 agent modules and their roles.

| Agent | Business Function | ADK Modules | Feedback Loop |
|-------|------------------|-------------|---------------|
| ResearchAgent | Market trend scanning | memory_buffer, scoring_toolkit | External validation |
| ContentAgent | Blog and ad generation | few_shot_selector, tone_modeler | Self-reflection |
| CampaignAgent | Campaign orchestration | orchestration_engine | Loop scoring |
| EngagementAgent | Email flows, retargeting | routing_agent | Reforge loop |
| OptimizationAgent | Ad tuning | realtime_feedback, metric_map | Metric-weighted tuning |
| AnalyticsAgent | Reporting | insight_collector | Summary validation |
| ConfigAgent | Prompt config tuning | config_mutator | Prompt genome refinement |

Use this overview to understand how each agent collaborates within the system.
