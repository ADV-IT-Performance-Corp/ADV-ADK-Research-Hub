"""Demonstrate agents collaborating via AsyncEventBus."""

import asyncio

from o3research.core import AsyncEventBus, get_logger
from o3research.agents.campaign_agent import CampaignAgent
from o3research.agents.engagement_agent import EngagementAgent
from o3research.agents.analytics_agent import AnalyticsAgent
from o3research.marketing import (
    GoogleAdsCampaignAgent,
    BudgetAllocatorAgent,
    CreativePromptAgent,
)


event_bus = AsyncEventBus()
logger = get_logger("MarketingWorkflow")

campaign_agent = CampaignAgent()
engagement_agent = EngagementAgent()
analytics_agent = AnalyticsAgent()
google_ads_agent = GoogleAdsCampaignAgent()
budget_agent = BudgetAllocatorAgent()
creative_agent = CreativePromptAgent()


async def handle_campaign(product: str) -> None:
    """Plan a campaign then trigger engagement."""
    # Advantage+ approach for dynamic creative optimization
    # docs/performance_marketing/meta_ai_strategy.md lines 8-11
    logger.info(campaign_agent.run(product))
    logger.info(google_ads_agent.run(product))
    await event_bus.publish("allocate", product)


async def handle_allocate(product: str) -> None:
    """Allocate budget then trigger engagement."""
    metrics = {
        "search": {"conversions": 30, "revenue": 1200},
        "social": {"conversions": 20, "revenue": 800},
    }
    logger.info(budget_agent.run(metrics, target=2, goal="ROAS"))
    await event_bus.publish("engage", f"prospect interested in {product}")


async def handle_engage(prospect: str) -> None:
    """Nurture the lead and forward metrics."""
    # Smart Bidding concepts apply to lead targeting
    # docs/performance_marketing/google_insights_summary.md lines 8-11
    logger.info(engagement_agent.run(prospect))
    logger.info(creative_agent.run(prospect, "busy marketer"))
    await event_bus.publish("report", f"conversion data for {prospect}")


async def handle_report(data: str) -> None:
    """Analyze campaign performance."""
    # Growth loops emphasize rapid test→analyze→deploy cycles
    # docs/performance_marketing/reforge_growth_loops.md lines 9-19
    logger.info(analytics_agent.run(data))


event_bus.subscribe("launch", handle_campaign)
event_bus.subscribe("allocate", handle_allocate)
event_bus.subscribe("engage", handle_engage)
event_bus.subscribe("report", handle_report)


async def main() -> None:
    await event_bus.publish("launch", "new SaaS product")


if __name__ == "__main__":
    asyncio.run(main())
