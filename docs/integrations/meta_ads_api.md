# Meta Ads API Integration

**Focus**: Retrieving performance metrics from Meta's marketing APIs

## Setup Steps
- Create a Meta developer application and generate an access token
- Grant permissions for the Marketing API
- Install the `facebook-business` Python SDK

## Example Usage
```python
from src.integrations.meta_ads_client import MetaAdsClient

client = MetaAdsClient(access_token="META_TOKEN")
metrics = client.fetch_campaign_metrics("111222333")
print(metrics)
```

The `MetaAdsClient` wraps API calls to pull key metrics such as clicks and conversions. Replace the placeholders with real credentials when deploying.
