import unittest
from unittest.mock import patch

from o3research.research import CompetitorScannerAgent


class TestCompetitorScannerAgent(unittest.TestCase):
    def test_run_extracts_title(self) -> None:
        agent = CompetitorScannerAgent()
        html = "<html><head><title>Example Corp</title></head><body></body></html>"
        with patch.object(CompetitorScannerAgent, "fetch_page", return_value=html):
            result = agent.run("http://example.com")
        self.assertIn("Example Corp", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
