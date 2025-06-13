# Performance Marketing Resources

This repo is built on Google ADK 1.3 + Vertex AI; all agents communicate via the Google Agent‐to‐Agent protocol (A2A v0.6).

This directory compiles research notes and strategies for data-driven advertising. The summaries below highlight key concepts for optimizing campaigns with AI and automation.

## Included Summaries

- `google_insights_summary.md`
- `meta_ai_strategy.md`
- `hubspot_ai_automation.md`
- `mckinsey_ai_marketing.md`
- `neurogym_neuromarketing.md`
- `reforge_growth_loops.md`
- `skai_roi_optimization.md`
- `smartly_creative_ai.md`
- `budget_allocation.md`
- `ppc_growth_loops.md`
- `ltv_models.md`
- `landing_page_content.md`
- `lead_capture_techniques.md`
- `assistant_architecture.md`
- `api_integration.md`
- `prompt_usage_examples.md`

## Usage

Use `GoogleAdsCampaignAgent` to quickly create a campaign outline:

```python
from o3research.marketing import GoogleAdsCampaignAgent

agent = GoogleAdsCampaignAgent()
print(agent.run("example offer"))
```

Use `MetaAdsAgent` to generate a Meta Advantage+ plan:

```python
from o3research.marketing import MetaAdsAgent

agent = MetaAdsAgent()
print(agent.run("new product"))
```

Allocate spend across channels with `BudgetAllocatorAgent`:

```python
from o3research.marketing import BudgetAllocatorAgent

metrics = {
    "search": {"conversions": 50, "revenue": 2000},
    "social": {"conversions": 20, "revenue": 900},
}

agent = BudgetAllocatorAgent()
print(agent.run(metrics, target=3, goal="ROAS"))
```

Compute spend shares from campaign plans with `Budgeter`:

```python
from o3research.marketing import Budgeter

plans = {
    "search": {
        "plan": "Search campaign",
        "metrics": {"impressions": 1000, "clicks": 100, "cost": 100.0, "conversions": 10, "revenue": 200.0},
    },
    "social": {
        "plan": "Social campaign",
        "metrics": {"impressions": 500, "clicks": 50, "cost": 50.0, "conversions": 5, "revenue": 80.0},
    },
}

budgeter = Budgeter()
print(budgeter.allocate(plans))
```

Plan a marketing funnel with `FunnelPlannerAgent`:

```python
from o3research.marketing import FunnelPlannerAgent

agent = FunnelPlannerAgent()
print(agent.run("software", "lead"))
```

Create short ad copy using `CreativePromptAgent`:

```python
from o3research.marketing import CreativePromptAgent

agent = CreativePromptAgent()
print(agent.run("smartwatch", "athlete"))
```

Push a campaign plan to the Google Ads API sandbox using `push_campaign`:

```python
from o3research.marketing import push_campaign

plan = {"name": "Sandbox Campaign", "customer_id": "123-456-7890"}
print(push_campaign(plan))
```

To log prompts for debugging, set the environment variable `PROMPT_OBSERVABILITY=1` before running any agent.
See the [Prompt Observability guide](../analytics/prompt_observability.md) for details on how the logging pipeline works.

For an end-to-end example, follow the [Quick Start section](../../README.md#-quick-start) in the repository root.
