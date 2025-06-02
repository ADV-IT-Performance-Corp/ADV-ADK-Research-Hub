# Google Ads API Integration

**Focus**: Accessing campaign data and managing ads via the Google Ads API

## Setup Steps
- Create a Google Cloud project and enable the Google Ads API
- Generate OAuth credentials and download the JSON key file
- Install the official Google Ads Python client

## Example Usage
```python
from src.integrations.google_ads_client import GoogleAdsClient

client = GoogleAdsClient(credentials_path="google.json")
metrics = client.fetch_campaign_metrics("1234567890")
print(metrics)
```

This example demonstrates fetching basic metrics. In a real deployment the client would call the live API and return impressions, clicks and conversions.
