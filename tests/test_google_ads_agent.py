import unittest

from o3research.marketing import GoogleAdsCampaignAgent
from o3research.agents.agent_registry import get_agent


class TestGoogleAdsCampaignAgent(unittest.TestCase):
    def test_plan_generation(self) -> None:
        agent = GoogleAdsCampaignAgent()
        plan = agent.run("cloud service")
        self.assertIn("Search", plan)
        self.assertIn("docs/performance_marketing/google_insights_summary.md", plan)

    def test_registry_lookup(self) -> None:
        cls = get_agent("google_ads")
        self.assertIs(cls, GoogleAdsCampaignAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
