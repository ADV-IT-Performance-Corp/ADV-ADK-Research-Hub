import unittest

from o3research.agents import EngagementAgent


class TestEngagementAgent(unittest.TestCase):
    def test_nurture_lead(self) -> None:
        agent = EngagementAgent()
        result = agent.run("hot lead")
        self.assertEqual(result, "EngagementAgent nurtures lead: hot lead")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
