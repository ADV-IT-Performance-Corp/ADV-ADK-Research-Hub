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

    def test_export_csv_multiple_rows(self):
        rows_in = [
            {"clicks": 5, "impressions": 10},
            {"clicks": 7, "impressions": 14},
        ]
        rg = ReportGenerator()
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "metrics.csv"
            rg.export_csv(rows_in, path)
            with path.open() as f:
                reader = csv.reader(f)
                rows = list(reader)

        expected = [
            ["clicks", "impressions"],
            ["5", "10"],
            ["7", "14"],
        ]
        self.assertEqual(rows, expected)

    def test_export_csv_empty_list(self):
        rg = ReportGenerator()
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "metrics.csv"
            with self.assertRaises(ValueError):
                rg.export_csv([], path)


if __name__ == "__main__":
    unittest.main()
