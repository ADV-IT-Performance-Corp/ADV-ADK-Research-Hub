"""BigQuery sink for analytics data."""

from o3research.analytics import BigQueryMetricsSink


class BigQuerySink(BigQueryMetricsSink):
    """Alias wrapper around :class:`BigQueryMetricsSink`."""

    pass


__all__ = ["BigQuerySink"]
