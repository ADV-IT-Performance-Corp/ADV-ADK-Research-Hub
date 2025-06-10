import asyncio
import unittest
from unittest.mock import patch

import assistant


class TestAssistantWorkflow(unittest.TestCase):
    @patch("assistant.push_campaign")
    def test_run_campaign(self, mock_push) -> None:
        mock_push.return_value = "customers/123/campaigns/1"
        result = asyncio.run(assistant.run_campaign("sample product"))
        self.assertIn("Campaign plan", result)
        self.assertIn("Budget allocations", result)
        self.assertIn("customers/123/campaigns/1", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
