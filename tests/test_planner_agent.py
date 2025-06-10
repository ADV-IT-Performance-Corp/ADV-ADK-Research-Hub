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


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
