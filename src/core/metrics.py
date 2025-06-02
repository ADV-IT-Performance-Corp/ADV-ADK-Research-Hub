class MetricsCollector:
    """Simple metrics collector that aggregates raw counts and computes KPIs."""

    def __init__(self) -> None:
        self.records = []

    def add(self, impressions: int, clicks: int, cost: float, conversions: int, revenue: float) -> None:
        """Add a new set of raw metrics."""
        self.records.append({
            "impressions": impressions,
            "clicks": clicks,
            "cost": cost,
            "conversions": conversions,
            "revenue": revenue,
        })

    def collect(self) -> dict:
        """Return aggregated metrics along with computed KPIs."""
        total_impressions = sum(r["impressions"] for r in self.records)
        total_clicks = sum(r["clicks"] for r in self.records)
        total_cost = sum(r["cost"] for r in self.records)
        total_conversions = sum(r["conversions"] for r in self.records)
        total_revenue = sum(r["revenue"] for r in self.records)

        ctr = (total_clicks / total_impressions) if total_impressions else 0.0
        cpc = (total_cost / total_clicks) if total_clicks else 0.0
        conversion_rate = (total_conversions / total_clicks) if total_clicks else 0.0
        roas = (total_revenue / total_cost) if total_cost else 0.0

        return {
            "impressions": total_impressions,
            "clicks": total_clicks,
            "cost": total_cost,
            "conversions": total_conversions,
            "revenue": total_revenue,
            "CTR": ctr,
            "CPC": cpc,
            "ConversionRate": conversion_rate,
            "ROAS": roas,
        }
