import unittest
from unittest.mock import patch

from o3research.analytics import GA4Client, compute_kpis, generate_report


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
    def test_generate_report(self, mock_load, mock_fetch) -> None:
        mock_fetch.return_value = MOCK_METRICS
        client = GA4Client("demo")
        report = generate_report(client, "2023-01-01", "2023-01-31")
        self.assertIn("| ROAS | 4.0 |", report)
        self.assertIn("| CTR |", report)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
