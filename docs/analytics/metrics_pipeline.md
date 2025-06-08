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

## Advanced KPIs

### Customer Lifetime Value (CLV)
CLV measures the revenue generated per customer over their lifetime.
`CLV = Total Revenue / Total Conversions`

### Cost per Acquisition (CPA)
CPA measures the average cost to acquire a customer.
`CPA = Total Cost / Total Conversions`

### Retention Metrics
Retention shows how many customers return after the initial conversion.
Typical formulas include:
- **Retention Rate** = Returning Customers / Total Conversions
- **Churn Rate** = 1 - Retention Rate

```python
collector.add(
    impressions=100,
    clicks=10,
    cost=5.0,
    conversions=2,
    revenue=20.0,
    returning_customers=1,
)
kpis = collector.collect()
```
