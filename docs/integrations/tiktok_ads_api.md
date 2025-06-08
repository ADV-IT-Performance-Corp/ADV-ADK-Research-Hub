# TikTok Ads API Integration

**URL:** https://ads.tiktok.com/marketing_api/
**Relevance:** campaign creation, analytics
**Used by Agents:** MarketingAgent, ReportingAgent

## Token Acquisition
1. Apply for a TikTok for Business developer account and create an app.
2. Record the generated **App ID** and **App Secret** from the developer portal.
3. Request advertiser authorization to access account data.
4. Exchange the authorization code for an access token using the `/oauth2/access_token/` endpoint.
5. Store and refresh the token securely with `/oauth2/refresh_token/` when needed.

## Example API Calls

```bash
# List advertisers connected to your app
curl -G "https://business-api.tiktok.com/open_api/v1.3/oauth2/advertiser/get/" \
  -d "access_token=$ACCESS_TOKEN"

# Retrieve campaigns for an advertiser
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/campaign/get/" \
  -H "Access-Token: $ACCESS_TOKEN" \
  -d '{"advertiser_id":"$ADVERTISER_ID"}'
```

## Security Guidance
- Do not embed tokens in code repositories.
- Use environment variables or a secrets manager for runtime access.
