# Agent System Overview

This overview summarizes the core modules and agent roles used in the O3 Deep Research project.

## Module Map
| Module | Description |
|-------|-------------|
| `base_agent.py` | Common execution framework for all agents |
| `semantic_cache.py` | Stores and retrieves prior prompt results |
| `few_shot_selector.py` | Chooses examples for few-shot prompts |
| `token_optimizer.py` | Minimizes token usage in prompts |
| `self_reflection.py` | Supports agent self‑evaluation |

## Agent Roles
| Agent | Purpose |
|-------|---------|
| **ResearchAgent** | Gathers market insights and competitor data |
| **ContentAgent** | Generates blog posts, ads, and social updates |
| **CampaignAgent** | Launches and iterates PPC campaigns |
| **EngagementAgent** | Manages retargeting and email sequences |
| **OptimizationAgent** | Tunes campaigns based on live metrics |
| **AnalyticsAgent** | Reports results and anomalies |
| **ConfigAgent** | Adjusts prompt settings and routing |

These roles collaborate via the ADK to automate the marketing workflow.
