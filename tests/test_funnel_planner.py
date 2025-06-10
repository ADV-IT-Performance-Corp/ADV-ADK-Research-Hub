import unittest

from o3research.marketing import FunnelPlannerAgent
from o3research.agents.agent_registry import get_agent


class TestFunnelPlannerAgent(unittest.TestCase):
    def test_plan_generation(self) -> None:
        agent = FunnelPlannerAgent()
        plan = agent.run("SaaS", "lead")
        self.assertIn("TOFU", plan)
        self.assertIn("MOFU", plan)
        self.assertIn("BOFU", plan)
        self.assertIn("docs/performance_marketing/reforge_growth_loops.md", plan)

    def test_registry_lookup(self) -> None:
        cls = get_agent("funnel_planner")
        self.assertIs(cls, FunnelPlannerAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
