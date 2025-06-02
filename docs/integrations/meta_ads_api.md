# Meta Ads API Integration

**URL:** https://developers.facebook.com/docs/marketing-api/
**Relevance:** audience targeting, ad optimization
**Used by Agents:** MarketingAgent, ReportingAgent

## Token Acquisition
1. Create a Meta developer app and add the **Marketing API** product.
2. Generate a system user and assign advertising permissions.
3. Use the Graph API Explorer or `meta-marketing` CLI to obtain a long-lived access token.
4. Store the app ID, app secret, and token securely in a vault or environment variables.
5. Refresh tokens periodically using the `/oauth/access_token` endpoint.

## Example API Calls

```bash
# List ad accounts for the business
curl "https://graph.facebook.com/v19.0/me/adaccounts?access_token=$ACCESS_TOKEN"

# Fetch campaign insights
curl "https://graph.facebook.com/v19.0/$ACCOUNT_ID/insights" \
  -d "access_token=$ACCESS_TOKEN" \

  -d "fields=campaign_name,impressions,clicks,spend"
```

## Security Guidance
- Never store tokens directly in code repositories.
- Prefer managed secrets services or encrypted environment variables.
