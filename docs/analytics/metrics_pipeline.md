# Automated Metrics Pipeline

This document explains how campaign metrics flow into the AnalyticsAgent for optimization.

1. **Data Collection**
   - `GoogleAdsClient` and `MetaAdsClient` pull raw metrics from the respective APIs.
   - Results are normalized and aggregated by `MetricsCollector`.
2. **Analysis**
   - The aggregated metrics are passed to `AnalyticsAgent` for reporting.
   - `OptimizationAgent` uses these metrics to adjust bids and budgets.

## Example
```python
collector = MetricsCollector()
collector.add_source(lambda: GoogleAdsClient('google.json').fetch_campaign_metrics('123'))
collector.add_source(lambda: MetaAdsClient('token').fetch_campaign_metrics('abc'))
metrics = collector.collect()
print(metrics)
```
