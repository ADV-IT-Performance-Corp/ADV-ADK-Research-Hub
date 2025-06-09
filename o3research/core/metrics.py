from typing import Dict, List, Union


class MetricsCollector:
    """Simple metrics collector that aggregates raw counts and computes KPIs."""

    def __init__(self) -> None:
        self.records: List[Dict[str, Union[int, float]]] = []

    def add(
        self,
        impressions: int,
        clicks: int,
        cost: float,
        conversions: int,
        revenue: float,
        returning_customers: int = 0,
    ) -> None:
        """Add a new set of raw metrics."""
        self.records.append(
            {
                "impressions": impressions,
                "clicks": clicks,
                "cost": cost,
                "conversions": conversions,
                "revenue": revenue,
                "returning_customers": returning_customers,
            }
        )

    def collect(self) -> Dict[str, Union[int, float]]:
        """Return aggregated metrics along with computed KPIs."""
        total_impressions = sum(r["impressions"] for r in self.records)
        total_clicks = sum(r["clicks"] for r in self.records)
        total_cost = sum(r["cost"] for r in self.records)
        total_conversions = sum(r["conversions"] for r in self.records)
        total_revenue = sum(r["revenue"] for r in self.records)
        total_returning = sum(r.get("returning_customers", 0) for r in self.records)

        ctr = (total_clicks / total_impressions) if total_impressions else 0.0
        cpc = (total_cost / total_clicks) if total_clicks else 0.0
        conversion_rate = (total_conversions / total_clicks) if total_clicks else 0.0
        roas = (total_revenue / total_cost) if total_cost else 0.0
        clv = (total_revenue / total_conversions) if total_conversions else 0.0
        cpa = (total_cost / total_conversions) if total_conversions else 0.0
        retention_rate = (
            (total_returning / total_conversions) if total_conversions else 0.0
        )

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
            "CLV": clv,
            "CPA": cpa,
            "RetentionRate": retention_rate,
        }
