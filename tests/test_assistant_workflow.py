import asyncio
import unittest
from unittest.mock import patch

import assistant


class TestAssistantWorkflowAsync(unittest.TestCase):
    @patch("assistant.push_campaign")
    def test_run_campaign_summary(self, mock_push) -> None:
        mock_push.return_value = "customers/999/campaigns/42"
        # ensure isolated event bus and cache
        assistant._event_bus = assistant.AsyncEventBus()
        assistant._cache = assistant.SemanticCache()
        result = asyncio.run(assistant.run_campaign("demo"))
        self.assertIn("Campaign plan for demo", result)
        self.assertIn("Creative suggestions", result)
        self.assertIn("customers/999/campaigns/42", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
