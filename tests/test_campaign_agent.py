import unittest

from o3research.agents import CampaignAgent


class TestCampaignAgent(unittest.TestCase):
    def test_plan_campaign(self) -> None:
        agent = CampaignAgent()
        result = agent.run("SaaS")
        self.assertIn("CampaignAgent plans a campaign", result)
        self.assertIn("SaaS", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
