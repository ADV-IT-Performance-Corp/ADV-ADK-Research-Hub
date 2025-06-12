# Marketing API Integration

**Focus**: Example of sending a campaign plan to the Google Ads API sandbox.

## push_campaign

Use `push_campaign` from `o3research.marketing`:

```python
from o3research.marketing import push_campaign

plan = {"name": "Sandbox Campaign", "customer_id": "123-456-7890"}
resource = push_campaign(plan)
print(resource)
```

## Service Account Authentication

`GoogleAdsClient` and `GAClient` can load a service-account JSON key. The
credentials are built with
`google.oauth2.service_account.Credentials` and refreshed automatically.

```python
from marketing_assistant import GoogleAdsClient

ads = GoogleAdsClient("creds.json", "token.json", service_account_file="sa.json")
```
