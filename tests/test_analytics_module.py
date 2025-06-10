import unittest

from o3research.analytics import GA4Client, compute_kpis, generate_report


class DummyClient(GA4Client):
    def __init__(self) -> None:
        super().__init__(property_id="demo")

    def fetch_metrics(self, start_date: str, end_date: str):
        return {
            "impressions": 1000,
            "clicks": 100,
            "cost": 50.0,
            "conversions": 10,
            "revenue": 200.0,
            "returning_customers": 5,
        }


class TestAnalyticsModule(unittest.TestCase):
    def test_compute_kpis(self):
        client = DummyClient()
        kpis = compute_kpis(client, "2023-01-01", "2023-01-31")
        self.assertAlmostEqual(kpis["ROAS"], 4.0)
        self.assertAlmostEqual(kpis["RetentionRate"], 0.5)

    def test_generate_report(self):
        client = DummyClient()
        report = generate_report(client, "2023-01-01", "2023-01-31")
        self.assertIn("| ROAS | 4.0 |", report)
        self.assertIn("| CTR |", report)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
