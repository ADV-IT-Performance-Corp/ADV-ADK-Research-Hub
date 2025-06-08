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
import json
import requests

API_KEY = "YOUR_API_KEY"
events = [{"user_id": "user123", "event_type": "Button Clicked"}]

requests.post(
    "https://api.amplitude.com/2/httpapi",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"api_key": API_KEY, "events": events}),
)
```
