import unittest

from google.adk.runners import InMemoryRunner
from google.genai import types
from google.adk.events.event import Event
from typing import cast

from o3research.core.base_agent import Agent
from o3research.agents.campaign_agent import CampaignAgent
from o3research.marketing import BudgetAllocatorAgent
from o3research.agents.engagement_agent import EngagementAgent
from o3research.agents.analytics_agent import AnalyticsAgent


class MarketingFlowAgent(Agent):
    """Simple flow agent executing marketing steps sequentially."""

    def __init__(self) -> None:
        super().__init__(name="MarketingFlowAgent")
        self.campaign_agent = CampaignAgent()
        self.budget_agent = BudgetAllocatorAgent()
        self.engagement_agent = EngagementAgent()
        self.analytics_agent = AnalyticsAgent()

    async def _run_async_impl(self, ctx):
        product = ""
        if ctx.user_content and ctx.user_content.parts:
            product = ctx.user_content.parts[0].text or ""
        metrics = {
            "search": {"conversions": 30, "revenue": 1200},
            "social": {"conversions": 20, "revenue": 800},
        }
        outputs = [
            self.campaign_agent.run(product),
            self.budget_agent.run(metrics, target=2, goal="ROAS"),
            self.engagement_agent.run(f"prospect interested in {product}"),
            self.analytics_agent.run(
                f"conversion data for prospect interested in {product}"
            ),
        ]
        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            content=types.Content(
                parts=[types.Part.from_text(text="\n".join(outputs))],
                role="model",
            ),
        )


class TestMarketingFlowRunner(unittest.TestCase):
    def test_run_flow(self) -> None:
        agent = MarketingFlowAgent()
        runner = InMemoryRunner(agent)
        runner.session_service.create_session_sync(  # type: ignore[attr-defined]
            app_name=runner.app_name, user_id="u", session_id="s"
        )
        msg = types.Content(
            parts=[types.Part.from_text(text="new SaaS product")], role="user"
        )
        events = list(runner.run(user_id="u", session_id="s", new_message=msg))
        content = cast(types.Content, events[-1].content)
        parts = cast(list[types.Part], content.parts)
        final_text = cast(str, parts[0].text)
        self.assertIn("campaign for new SaaS product", final_text)
        self.assertIn("Recommended spend per channel", final_text)
        self.assertIn("AnalyticsAgent analyzed data", final_text)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
