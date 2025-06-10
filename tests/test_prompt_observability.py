import os
import unittest
from unittest.mock import patch

from o3research.marketing import GoogleAdsCampaignAgent
from o3research.core.telemetry import configure_prompt_collector, get_prompt_client


class DummyCollector:
    def __init__(self) -> None:
        self.events = []

    def __call__(self, event):
        self.events.append(event)


class TestPromptObservability(unittest.TestCase):
    def test_prompt_logging(self) -> None:
        collector = DummyCollector()
        configure_prompt_collector(collector)
        agent = GoogleAdsCampaignAgent()
        with patch.dict(
            os.environ, {"PROMPT_OBSERVABILITY": "1", "TELEMETRY_ENABLED": "1"}
        ):
            result = agent.run("obs product")
            get_prompt_client().flush()
        self.assertEqual(len(collector.events), 1)
        event = collector.events[0]
        self.assertEqual(event["prompt_id"], "google_ads_plan")
        self.assertEqual(event["agent_name"], "GoogleAdsCampaignAgent")
        self.assertEqual(event["tokens"], len(result.split()))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
