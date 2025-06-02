# Metrics Pipeline

This page outlines how raw campaign metrics are turned into KPIs.

## Raw Metrics
- **Impressions**
- **Clicks**
- **Cost**
- **Conversions**
- **Revenue**

## KPI Calculations
- **CTR (Click-Through Rate)** = Clicks / Impressions
- **CPC (Cost Per Click)** = Cost / Clicks
- **Conversion Rate** = Conversions / Clicks
- **ROAS (Return on Ad Spend)** = Revenue / Cost

The `MetricsCollector.collect()` method aggregates raw values and computes these KPIs for use by analytics agents.
