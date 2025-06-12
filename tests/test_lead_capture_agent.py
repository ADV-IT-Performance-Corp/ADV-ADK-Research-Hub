import unittest

from o3research.marketing import LeadCaptureAgent
from o3research.agents.agent_registry import get_agent


class TestLeadCaptureAgent(unittest.TestCase):
    def test_flow_generation(self) -> None:
        agent = LeadCaptureAgent()
        result = agent.run("form")
        self.assertIn("Lead capture via form", result)
        self.assertIn("docs/performance_marketing/lead_capture_techniques.md", result)

    def test_registry_lookup(self) -> None:
        cls = get_agent("lead_capture")
        self.assertIs(cls, LeadCaptureAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
