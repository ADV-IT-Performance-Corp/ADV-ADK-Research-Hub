import unittest

from o3research.agents.prompt_to_plan_agent import PromptToPlanAgent


class TestPromptToPlanAgent(unittest.TestCase):
    def test_run_returns_plan(self) -> None:
        agent = PromptToPlanAgent()
        result = agent.run("launch new product")
        self.assertIn("Action plan", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
