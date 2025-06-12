from pathlib import Path
from typing import Any, Dict, List, Optional

from google.oauth2.credentials import Credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
from google.auth.transport.requests import Request  # type: ignore
from googleapiclient.discovery import build  # type: ignore

SCOPES = ["https://www.googleapis.com/auth/adwords"]


class GoogleAdsClient:
    """Simplified Google Ads API client using OAuth 2.0 or a service account."""

    def __init__(
        self,
        credentials_file: str,
        token_file: str,
        service_account_file: Optional[str] = None,
    ) -> None:
        self.credentials_file = credentials_file
        self.token_file = token_file
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
                "googleads", "v14", credentials=self.creds, cache_discovery=False
            )
        return self._service

    def refresh_token(self) -> None:
        if not self.creds:
            raise RuntimeError("Credentials not loaded")
        if self.creds.expired:
            self.creds.refresh(Request())
            if getattr(self.creds, "refresh_token", None):
                Path(self.token_file).write_text(self.creds.to_json())

    def list_campaigns(
        self, customer_id: str, page_size: int = 100
    ) -> List[Dict[str, Any]]:
        """Return campaigns for *customer_id* using Google Ads API."""
        self.refresh_token()
        query = (
            "SELECT campaign.id, campaign.name FROM campaign ORDER BY "
            f"campaign.id LIMIT {page_size}"
        )
        body = {"query": query}
        request = (
            self.service.customers()
            .googleAds()
            .search(customerId=customer_id, body=body)
        )
        response = request.execute()
        return response.get("results", [])
