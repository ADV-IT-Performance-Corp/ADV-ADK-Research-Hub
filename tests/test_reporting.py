import csv
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from o3research.core.reporting import ReportGenerator


class TestReportGenerator(unittest.TestCase):
    def test_to_markdown(self):
        metrics = {"clicks": 5, "impressions": 10}
        rg = ReportGenerator()
        md = rg.to_markdown(metrics)
        expected = (
            "| Metric | Value |\n"
            "| --- | --- |\n"
            "| clicks | 5 |\n"
            "| impressions | 10 |"
        )
        self.assertEqual(md, expected)

    def test_export_csv(self):
        metrics = {"clicks": 5, "impressions": 10}
        rg = ReportGenerator()
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "metrics.csv"
            rg.export_csv(metrics, path)
            with path.open() as f:
                reader = csv.reader(f)
                rows = list(reader)
        self.assertEqual(rows[0], ["clicks", "impressions"])
        self.assertEqual(rows[1], ["5", "10"])


if __name__ == "__main__":
    unittest.main()
