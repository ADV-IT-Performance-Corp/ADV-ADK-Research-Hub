from typing import Dict


class GoogleAdsClient:
    """Placeholder client for the Google Ads API."""

    def __init__(self, credentials_path: str) -> None:
        self.credentials_path = credentials_path

    def fetch_campaign_metrics(self, customer_id: str) -> Dict[str, float]:
        """Return basic metrics for a campaign.

        In a real environment this would make authenticated API calls.
        """
        return {"impressions": 0.0, "clicks": 0.0, "conversions": 0.0}
