import unittest

from o3research.marketing import CreativePromptAgent
from o3research.agents.agent_registry import get_agent


class TestCreativePromptAgent(unittest.TestCase):
    def test_copy_generation(self) -> None:
        agent = CreativePromptAgent()
        result = agent.run("AI tool", "busy marketer")
        self.assertIn("Ad copy variants", result)
        self.assertIn("AI tool", result)
        self.assertIn("busy marketer", result)
        self.assertIn("docs/performance_marketing/neurogym_neuromarketing.md", result)

    def test_registry_lookup(self) -> None:
        cls = get_agent("creative_prompt")
        self.assertIs(cls, CreativePromptAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
