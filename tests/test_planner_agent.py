import unittest
from unittest.mock import patch

from o3research.agents.marketing_assistant import PlannerAgent


class TestPlannerAgent(unittest.TestCase):
    def test_campaign_plan_logged(self) -> None:
        agent = PlannerAgent()
        with patch(
            "o3research.agents.marketing_assistant.planner.log_prompt"
        ) as mock_log:
            plan = agent.run("demo")
        self.assertIn("Campaign plan for demo", plan)
        mock_log.assert_called_once()

    def test_run_returns_expected_lines(self) -> None:
        agent = PlannerAgent()
        with patch("o3research.agents.marketing_assistant.planner.log_prompt"):
            plan = agent.run("demo")
        expected_lines = [
            "Campaign plan for demo:",
            "- Research target audience and key pain points",
            "- Develop messaging themes and creative assets",
            "- Launch across search, social, and email channels",
            "- Measure KPIs: impressions, clicks, and conversions",
        ]
        self.assertEqual(plan.splitlines(), expected_lines)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
