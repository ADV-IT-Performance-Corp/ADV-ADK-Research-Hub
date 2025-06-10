import unittest

from o3research.marketing import CreativeAgent
from o3research.agents.agent_registry import get_agent


class TestCreativeAgent(unittest.TestCase):
    def test_suggestions(self) -> None:
        agent = CreativeAgent()
        result = agent.run("analytics suite", "growth hacker")
        self.assertIn("Creative suggestions", result)
        self.assertIn("analytics suite", result)
        self.assertIn("growth hacker", result)

    def test_registry_lookup(self) -> None:
        cls = get_agent("creative")
        self.assertIs(cls, CreativeAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
