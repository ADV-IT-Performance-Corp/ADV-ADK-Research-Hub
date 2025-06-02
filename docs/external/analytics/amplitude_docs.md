# Amplitude Docs

**URL:** https://www.docs.developers.amplitude.com  
**Relevance:** analytics, performance  
**Used by Agents:** AnalyticsAgent, OptimizationAgent

## Description
Amplitude provides product analytics for measuring user engagement and conversion. Their developer docs outline APIs for ingesting events and querying insights.

## Use Cases
- Track agent-driven funnel metrics
- Analyze prompt impact on user behavior

## Integration Ideas
- Automate data exports for model performance monitoring

## See Also
- [Agent System Overview](../agent_system_overview.md)

## Example Code

```python
import requests

# Send a basic test event
payload = {
    "api_key": "YOUR_API_KEY",
    "events": [
        {"event_type": "agent_heartbeat", "user_id": "demo"}
    ]
}
requests.post("https://api2.amplitude.com/2/httpapi", json=payload)
```
