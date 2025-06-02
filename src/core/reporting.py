from typing import Dict


class ReportGenerator:
    """Create simple text reports from metrics."""

    def generate(self, metrics: Dict[str, float]) -> str:
        return (
            f"Impressions: {metrics.get('impressions', 0)}\n"
            f"Clicks: {metrics.get('clicks', 0)}\n"
            f"Conversions: {metrics.get('conversions', 0)}"
        )
