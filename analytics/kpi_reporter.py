"""Generate KPI reports using GA4 and BigQuery."""

from o3research.analytics import GA4Client, BigQueryMetricsSink, generate_report


class KPIReporter:
    """Convenience wrapper combining GA4 and BigQuery clients."""

    def __init__(self, property_id: str, table_id: str) -> None:
        self.ga_client = GA4Client(property_id)
        self.bq_sink = BigQueryMetricsSink(table_id)

    def report(self, start_date: str, end_date: str) -> str:
        """Return a Markdown report of KPIs and persist them."""
        return generate_report(
            self.ga_client,
            start_date,
            end_date,
            sink=self.bq_sink,
        )


__all__ = ["KPIReporter"]
