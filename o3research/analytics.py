from typing import Mapping

from .core.metrics import MetricsCollector
from .core.reporting import ReportGenerator


class GA4Client:
    """Client for Google Analytics 4."""

    def __init__(self, property_id: str) -> None:
        self.property_id = property_id
        # Initialization for GA4 API goes here

    def fetch_metrics(self, start_date: str, end_date: str) -> Mapping[str, float]:
        """Return raw metrics for the property.

        This method should be replaced with real GA4 API calls.
        """
        raise NotImplementedError("GA4 client integration pending")


def compute_kpis(
    client: GA4Client, start_date: str, end_date: str
) -> Mapping[str, float]:
    """Fetch metrics using *client* and compute KPIs."""
    metrics = client.fetch_metrics(start_date, end_date)
    collector = MetricsCollector()
    collector.add(
        impressions=int(metrics.get("impressions", 0)),
        clicks=int(metrics.get("clicks", 0)),
        cost=float(metrics.get("cost", 0.0)),
        conversions=int(metrics.get("conversions", 0)),
        revenue=float(metrics.get("revenue", 0.0)),
        returning_customers=int(metrics.get("returning_customers", 0)),
    )
    return collector.collect()


def generate_report(client: GA4Client, start_date: str, end_date: str) -> str:
    """Return a Markdown report of KPIs fetched from GA4."""
    kpis = compute_kpis(client, start_date, end_date)
    reporter = ReportGenerator()
    return reporter.to_markdown(kpis)


__all__ = ["GA4Client", "compute_kpis", "generate_report"]
