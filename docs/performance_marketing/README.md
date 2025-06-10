# Performance Marketing Resources

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

To log prompts for debugging, set the environment variable `PROMPT_OBSERVABILITY=1` before running any agent.
