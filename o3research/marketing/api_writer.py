import logging
from typing import Any, Dict, List

from google.ads.googleads.client import GoogleAdsClient  # type: ignore[import]
from google.ads.googleads.errors import GoogleAdsException  # type: ignore[import]

from ..core.telemetry import TelemetryClient

logger = logging.getLogger(__name__)

telemetry = TelemetryClient(lambda event: logger.info("%s", event))


def push_campaign(plan: Dict[str, Any]) -> str:
    """Push *plan* as a campaign via Google Ads API sandbox.

    Parameters
    ----------
    plan:
        Dictionary describing campaign config including ``customer_id``
        and ``name``.
    Returns
    -------
    str
        Resource name of the created campaign.
    """

    client = GoogleAdsClient.load_from_dict(
        {
            "developer_token": plan.get("developer_token", "INTEGRATION_TEST"),
            "login_customer_id": plan.get("customer_id", "000-000-0000"),
            "use_proto_plus": True,
        },
        version="v16",
    )

    campaign_service = client.get_service("CampaignService")
    operation = client.get_type("CampaignOperation")
    campaign = operation.create
    campaign.name = plan.get("name", "Sandbox Campaign")
    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    campaign.status = client.enums.CampaignStatusEnum.PAUSED

    telemetry.log_event(
        {
            "type": "request",
            "method": "mutate_campaigns",
            "payload": {"name": campaign.name},
        }
    )
    try:
        response = campaign_service.mutate_campaigns(
            customer_id=plan.get("customer_id", "000-000-0000"),
            operations=[operation],
            validate_only=True,
        )
        resource_names: List[str] = [
            result.resource_name for result in response.results
        ]
        telemetry.log_event(
            {
                "type": "response",
                "results": resource_names,
            }
        )
        telemetry.flush()
        return resource_names[0]
    except GoogleAdsException as exc:  # pragma: no cover - network errors
        telemetry.log_event({"type": "error", "message": str(exc)})
        telemetry.flush()
        raise
