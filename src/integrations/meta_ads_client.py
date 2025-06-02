from typing import Dict


class MetaAdsClient:
    """Placeholder client for Meta Ads API."""

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    def fetch_campaign_metrics(self, ad_account_id: str) -> Dict[str, float]:
        """Return campaign metrics.

        In production this would query Meta's Marketing API.
        """
        return {"impressions": 0.0, "clicks": 0.0, "conversions": 0.0}
