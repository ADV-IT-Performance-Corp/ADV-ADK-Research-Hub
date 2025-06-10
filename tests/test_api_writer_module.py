import os
import unittest
from unittest.mock import MagicMock, patch

from o3research.marketing.api_writer import push_campaign, telemetry


class TestApiWriter(unittest.TestCase):
    @patch("o3research.marketing.api_writer.GoogleAdsClient")
    def test_push_campaign_logs(self, mock_client_cls):
        events = []
        mock_client = mock_client_cls.load_from_dict.return_value
        service = mock_client.get_service.return_value
        service.mutate_campaigns.return_value.results = [
            MagicMock(resource_name="customers/123/campaigns/1")
        ]

        def collector(event):
            events.append(event)

        with patch.object(telemetry, "collector", collector, create=False), patch.dict(
            os.environ, {"TELEMETRY_ENABLED": "1"}
        ):
            res = push_campaign({"customer_id": "123", "name": "Test"})

        self.assertEqual(res, "customers/123/campaigns/1")
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0]["type"], "request")
        self.assertEqual(events[1]["type"], "response")
        self.assertIn("timing", events[1])
        self.assertIn("cost", events[1])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
