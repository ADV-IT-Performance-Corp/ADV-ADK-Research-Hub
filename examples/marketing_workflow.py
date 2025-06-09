"""Demonstrate agents collaborating via AsyncEventBus."""
import asyncio

from o3research.core import AsyncEventBus, get_logger
from o3research.agents.campaign_agent import CampaignAgent
from o3research.agents.engagement_agent import EngagementAgent
from o3research.agents.analytics_agent import AnalyticsAgent


event_bus = AsyncEventBus()
logger = get_logger("MarketingWorkflow")

campaign_agent = CampaignAgent()
engagement_agent = EngagementAgent()
analytics_agent = AnalyticsAgent()


async def handle_campaign(product: str) -> None:
    """Plan a campaign then trigger engagement."""
    # Advantage+ approach for dynamic creative optimization
    # docs/performance_marketing/meta_ai_strategy.md lines 8-11
    logger.info(campaign_agent.run(product))
    await event_bus.publish("engage", f"prospect interested in {product}")


async def handle_engage(prospect: str) -> None:
    """Nurture the lead and forward metrics."""
    # Smart Bidding concepts apply to lead targeting
    # docs/performance_marketing/google_insights_summary.md lines 8-11
    logger.info(engagement_agent.run(prospect))
    await event_bus.publish("report", f"conversion data for {prospect}")


async def handle_report(data: str) -> None:
    """Analyze campaign performance."""
    # Growth loops emphasize rapid test→analyze→deploy cycles
    # docs/performance_marketing/reforge_growth_loops.md lines 9-19
    logger.info(analytics_agent.run(data))


event_bus.subscribe("launch", handle_campaign)
event_bus.subscribe("engage", handle_engage)
event_bus.subscribe("report", handle_report)


async def main() -> None:
    await event_bus.publish("launch", "new SaaS product")


if __name__ == "__main__":
    asyncio.run(main())
