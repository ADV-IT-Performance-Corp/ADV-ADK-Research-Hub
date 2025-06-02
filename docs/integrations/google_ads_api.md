# Google Ads API Integration

**URL:** https://developers.google.com/google-ads/api
**Relevance:** campaign management, analytics
**Used by Agents:** MarketingAgent, ReportingAgent

## Token Acquisition
1. Create a Google Cloud project and enable the **Google Ads API**.
2. Configure OAuth consent and download your `client_id` and `client_secret` JSON.
3. Generate a refresh token using the OAuth playground or `google-ads` CLI.
4. Store `client_id`, `client_secret`, and refresh token in a secure secrets manager.
5. Exchange the refresh token for an access token at runtime.

## Example API Calls

```bash
# List accessible customer accounts
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  "https://googleads.googleapis.com/v16/customers:listAccessibleCustomers"

# Retrieve campaigns for an account
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  "https://googleads.googleapis.com/v16/customers/$CID/googleAds:search" \

  -d '{"query":"SELECT campaign.id, campaign.name FROM campaign"}'
```

## Security Guidance
- Avoid committing credentials to source control.
- Use environment variables or a vault service to inject tokens at runtime.
