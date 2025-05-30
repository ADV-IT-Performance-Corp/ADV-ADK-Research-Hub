# Amplitude Docs

**URL:** https://www.docs.developers.amplitude.com
**Relevance:** analytics, performance
**Used by Agents:** AnalyticsAgent, OptimizationAgent

## Description
Amplitude provides product analytics for measuring user engagement and conversion. Their developer docs outline APIs for ingesting events and querying insights. See [Reforge Growth Loops](../../performance_marketing/reforge_growth_loops.md) for marketing strategies that complement Amplitude metrics.

## Use Cases
- Track agent-driven funnel metrics
- Analyze prompt impact on user behavior

## Integration Ideas
- Automate data exports for model performance monitoring

## Example Code

```python
import amplitude
client = amplitude.Amplitude('API_KEY')
client.track(event={"user_id": "123", "event_type": "Ad Viewed"})
```
