"""Utilities for syncing metrics from Google Analytics 4."""

from typing import Mapping

from o3research.analytics import GA4Client, compute_kpis, BigQueryMetricsSink


def sync_metrics(
    property_id: str,
    start_date: str,
    end_date: str,
    *,
    table_id: str | None = None,
) -> Mapping[str, float]:
    """Fetch metrics from GA4 and optionally write them to BigQuery."""
    client = GA4Client(property_id)
    sink = BigQueryMetricsSink(table_id) if table_id else None
    return compute_kpis(client, start_date, end_date, sink=sink)


__all__ = ["sync_metrics"]
