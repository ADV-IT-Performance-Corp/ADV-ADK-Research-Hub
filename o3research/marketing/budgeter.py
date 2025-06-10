from typing import Any, Dict

from ..core.metrics import MetricsCollector


class Budgeter:
    """Compute budget allocations from campaign plans."""

    def allocate(self, plans: Dict[str, Dict[str, Any]]) -> Dict[str, float]:
        """Return allocation percentage per channel based on cost share."""
        costs: Dict[str, float] = {}
        total_cost = 0.0
        for channel, data in plans.items():
            metrics = data.get("metrics", {})
            collector = MetricsCollector()
            collector.add(
                impressions=int(metrics.get("impressions", 0)),
                clicks=int(metrics.get("clicks", 0)),
                cost=float(metrics.get("cost", 0.0)),
                conversions=int(metrics.get("conversions", 0)),
                revenue=float(metrics.get("revenue", 0.0)),
                returning_customers=int(metrics.get("returning_customers", 0)),
            )
            kpis = collector.collect()
            cost = float(kpis["cost"])
            costs[channel] = cost
            total_cost += cost

        allocations: Dict[str, float] = {}
        for channel, cost in costs.items():
            share = cost / total_cost if total_cost else 0.0
            allocations[channel] = round(share * 100, 2)
        return allocations
