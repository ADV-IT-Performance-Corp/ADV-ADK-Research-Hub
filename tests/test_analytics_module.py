import unittest
from unittest.mock import MagicMock, patch

from o3research.analytics import (
    GA4Client,
    BigQueryMetricsSink,
    compute_kpis,
    generate_report,
)


MOCK_METRICS = {
    "impressions": 1000,
    "clicks": 100,
    "cost": 50.0,
    "conversions": 10,
    "revenue": 200.0,
    "returning_customers": 5,
}


class TestAnalyticsModule(unittest.TestCase):
    @patch("o3research.analytics.GA4Client.fetch_metrics")
    @patch("o3research.analytics.GA4Client._load_credentials")
    def test_compute_kpis(self, mock_load, mock_fetch) -> None:
        mock_fetch.return_value = MOCK_METRICS
        client = GA4Client("demo")
        kpis = compute_kpis(client, "2023-01-01", "2023-01-31")
        self.assertAlmostEqual(kpis["ROAS"], 4.0)
        self.assertAlmostEqual(kpis["RetentionRate"], 0.5)

    @patch("o3research.analytics.GA4Client.fetch_metrics")
    @patch("o3research.analytics.GA4Client._load_credentials")
    def test_compute_kpis_with_sink(self, mock_load, mock_fetch) -> None:
        mock_fetch.return_value = MOCK_METRICS
        client = GA4Client("demo")
        mock_client = MagicMock()
        mock_client.insert_rows_json.return_value = []
        sink = BigQueryMetricsSink("proj.dataset.table", client=mock_client)
        kpis = compute_kpis(client, "2023-01-01", "2023-01-31", sink=sink)
        mock_client.insert_rows_json.assert_called_once()
        self.assertIn("ROAS", kpis)

    @patch("o3research.analytics.GA4Client.fetch_metrics")
    @patch("o3research.analytics.GA4Client._load_credentials")
    def test_generate_report(self, mock_load, mock_fetch) -> None:
        mock_fetch.return_value = MOCK_METRICS
        client = GA4Client("demo")
        report = generate_report(client, "2023-01-01", "2023-01-31")
        self.assertIn("| ROAS | 4.0 |", report)
        self.assertIn("| CTR |", report)

    @patch("o3research.analytics.GA4Client.fetch_metrics")
    @patch("o3research.analytics.GA4Client._load_credentials")
    def test_generate_report_with_sink(self, mock_load, mock_fetch) -> None:
        mock_fetch.return_value = MOCK_METRICS
        client = GA4Client("demo")
        mock_client = MagicMock()
        mock_client.insert_rows_json.return_value = []
        sink = BigQueryMetricsSink("proj.dataset.table", client=mock_client)
        report = generate_report(client, "2023-01-01", "2023-01-31", sink=sink)
        mock_client.insert_rows_json.assert_called_once()
        self.assertIn("| ROAS | 4.0 |", report)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
