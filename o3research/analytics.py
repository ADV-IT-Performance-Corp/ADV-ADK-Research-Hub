from __future__ import annotations

from pathlib import Path
from typing import Mapping, Optional

from google.cloud import bigquery  # type: ignore

from google.oauth2.credentials import Credentials  # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
from google.auth.transport.requests import Request  # type: ignore
from googleapiclient.discovery import build  # type: ignore

from .core.metrics import MetricsCollector
from .core.reporting import ReportGenerator


SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


class BigQueryMetricsSink:
    """Write metrics to a BigQuery table."""

    def __init__(self, table_id: str, client: bigquery.Client | None = None) -> None:
        self.table_id = table_id
        self.client = client or bigquery.Client()

    def write(self, metrics: Mapping[str, float]) -> None:
        """Insert *metrics* into the configured table."""
        errors = self.client.insert_rows_json(self.table_id, [dict(metrics)])
        if errors:  # pragma: no cover - error path hard to trigger in tests
            raise RuntimeError(f"Failed to insert rows: {errors}")


class GA4Client:
    """Client for Google Analytics 4."""

    def __init__(
        self,
        property_id: str,
        credentials_file: str = "ga_credentials.json",
        token_file: str = "ga_token.json",
    ) -> None:
        self.property_id = property_id
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.creds: Optional[Credentials] = None
        self._service = None
        self._load_credentials()

    def _load_credentials(self) -> None:
        token_path = Path(self.token_file)
        if token_path.exists():
            self.creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            assert self.creds is not None
            token_path.write_text(self.creds.to_json())

    @property
    def service(self):
        if not self._service:
            self._service = build(
                "analyticsdata", "v1beta", credentials=self.creds, cache_discovery=False
            )
        return self._service

    def fetch_metrics(self, start_date: str, end_date: str) -> Mapping[str, float]:
        """Return raw metrics for the property using the GA4 Data API."""
        body = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "metrics": [
                {"name": "impressions"},
                {"name": "clicks"},
                {"name": "adCost"},
                {"name": "conversions"},
                {"name": "totalRevenue"},
                {"name": "returningUsers"},
            ],
        }

        request = self.service.properties().runReport(
            property=f"properties/{self.property_id}", body=body
        )
        response = request.execute()

        rows = response.get("rows", [])
        if not rows:
            return {}

        values = [float(v.get("value", "0")) for v in rows[0].get("metricValues", [])]
        metrics = {
            "impressions": values[0] if len(values) > 0 else 0.0,
            "clicks": values[1] if len(values) > 1 else 0.0,
            "cost": values[2] if len(values) > 2 else 0.0,
            "conversions": values[3] if len(values) > 3 else 0.0,
            "revenue": values[4] if len(values) > 4 else 0.0,
            "returning_customers": values[5] if len(values) > 5 else 0.0,
        }
        return metrics


def compute_kpis(
    client: GA4Client,
    start_date: str,
    end_date: str,
    *,
    sink: Optional[BigQueryMetricsSink] = None,
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
    kpis = collector.collect()
    if sink:
        sink.write(kpis)
    return kpis


def generate_report(
    client: GA4Client,
    start_date: str,
    end_date: str,
    *,
    sink: Optional[BigQueryMetricsSink] = None,
) -> str:
    """Return a Markdown report of KPIs fetched from GA4."""
    kpis = compute_kpis(client, start_date, end_date, sink=sink)
    reporter = ReportGenerator()
    return reporter.to_markdown(kpis)


__all__ = [
    "GA4Client",
    "BigQueryMetricsSink",
    "compute_kpis",
    "generate_report",
]
