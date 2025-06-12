from pathlib import Path
from typing import Any, Dict, List, Optional

from google.oauth2.credentials import Credentials  # type: ignore

__version__ = "3.5.10"
from google.oauth2 import service_account  # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
from google.auth.transport.requests import Request  # type: ignore
from googleapiclient.discovery import build  # type: ignore

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


class GAClient:
    """Simplified Google Analytics Data API client.

    Supports OAuth 2.0 or a service account for authentication.
    """

    def __init__(
        self,
        credentials_file: str,
        token_file: str,
        property_id: str,
        service_account_file: Optional[str] = None,
    ) -> None:
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.property_id = property_id
        self.service_account_file = service_account_file
        self.creds: Optional[Credentials] = None
        self._service = None
        self._load_credentials()

    def _load_credentials(self) -> None:
        if self.service_account_file:
            self.creds = service_account.Credentials.from_service_account_file(
                self.service_account_file, scopes=SCOPES
            )
            return

        token_path = Path(self.token_file)
        if token_path.exists():
            self.creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        if not self.creds or not self.creds.valid:
            if (
                self.creds
                and self.creds.expired
                and getattr(self.creds, "refresh_token", None)
            ):
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

    def refresh_token(self) -> None:
        if not self.creds:
            raise RuntimeError("Credentials not loaded")
        if self.creds.expired:
            self.creds.refresh(Request())
            if getattr(self.creds, "refresh_token", None):
                Path(self.token_file).write_text(self.creds.to_json())

    def fetch_traffic(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Return daily sessions from GA4 for the configured property."""
        self.refresh_token()
        body = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "metrics": [{"name": "sessions"}],
            "dimensions": [{"name": "date"}],
        }
        request = self.service.properties().runReport(
            property=f"properties/{self.property_id}", body=body
        )
        response = request.execute()
        return response.get("rows", [])

    def fetch_conversions(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Return daily conversions from GA4 for the configured property."""
        self.refresh_token()
        body = {
            "dateRanges": [{"startDate": start_date, "endDate": end_date}],
            "metrics": [{"name": "conversions"}],
            "dimensions": [{"name": "date"}],
        }
        request = self.service.properties().runReport(
            property=f"properties/{self.property_id}", body=body
        )
        response = request.execute()
        return response.get("rows", [])
