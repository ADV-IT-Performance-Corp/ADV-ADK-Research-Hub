import unittest

from o3research.web.analytics_tagging import add_ga4_tag


class TestAnalyticsTagging(unittest.TestCase):
    def test_add_ga4_tag(self) -> None:
        html = "<html><head></head><body></body></html>"
        result = add_ga4_tag(html, "G-123", events=["click"])
        self.assertIn("G-123", result)
        self.assertIn("gtag('event'", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
