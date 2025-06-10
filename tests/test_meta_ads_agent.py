import unittest

from o3research.marketing import MetaAdsAgent
from o3research.agents.agent_registry import get_agent


class TestMetaAdsAgent(unittest.TestCase):
    def test_plan_generation(self) -> None:
        agent = MetaAdsAgent()
        plan = agent.run("mobile app")
        self.assertIn("Advantage+", plan)
        self.assertIn("dynamic creative", plan.lower())
        self.assertIn("audience expansion", plan.lower())
        self.assertIn("docs/performance_marketing/meta_ai_strategy.md", plan)

    def test_registry_lookup(self) -> None:
        cls = get_agent("meta_ads")
        self.assertIs(cls, MetaAdsAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
