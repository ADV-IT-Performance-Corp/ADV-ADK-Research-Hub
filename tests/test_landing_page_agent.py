import unittest

from o3research.marketing import LandingPageAgent
from o3research.agents.agent_registry import get_agent


class TestLandingPageAgent(unittest.TestCase):
    def test_content_generation(self) -> None:
        agent = LandingPageAgent()
        result = agent.run("product", "value")
        self.assertIn("Landing page for product", result)
        self.assertIn("docs/performance_marketing/landing_page_content.md", result)

    def test_registry_lookup(self) -> None:
        cls = get_agent("landing_page")
        self.assertIs(cls, LandingPageAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
