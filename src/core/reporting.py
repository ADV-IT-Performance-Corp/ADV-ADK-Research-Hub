import csv
from collections.abc import Iterable, Mapping


class ReportGenerator:
    """Generate reports from metrics and export them."""

    def to_markdown(self, metrics: Mapping[str, float]) -> str:
        """Return metrics formatted as a Markdown table."""
        header = "| Metric | Value |"
        separator = "| --- | --- |"
        lines = [header, separator]
        for key, value in metrics.items():
            lines.append(f"| {key} | {value} |")
        return "\n".join(lines)

    def export_csv(
        self, metrics: Mapping[str, float] | Iterable[Mapping[str, float]], path: str
    ) -> None:
        """Write metrics to a CSV file."""
        if isinstance(metrics, Mapping):
            rows = [metrics]
        else:
            rows = list(metrics)
            if not rows:
                raise ValueError("No metrics to export")

        fieldnames = list(rows[0].keys())
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
