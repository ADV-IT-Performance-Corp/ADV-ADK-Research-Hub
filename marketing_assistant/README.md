# Marketing Assistant Clients

This module provides lightweight wrappers for the Google Ads and Google Analytics Data APIs.
Both clients handle OAuth 2.0 or service-account authentication.

## GoogleAdsClient

`GoogleAdsClient` manages authentication and exposes a simple `list_campaigns` method.

```python
from marketing_assistant import GoogleAdsClient

ads = GoogleAdsClient("client_secret.json", "token.json")
for campaign in ads.list_campaigns("123-456-7890"):
    print(campaign)
```

## GAClient

`GAClient` connects to the GA4 Data API. Use `fetch_traffic` and `fetch_conversions` to retrieve metrics.

```python
from marketing_assistant import GAClient

ga = GAClient("client_secret.json", "token.json", "123456")
traffic = ga.fetch_traffic("2024-01-01", "2024-01-31")
```
