from collections.abc import Iterable, Mapping
from typing import Any

from ..core.metrics import MetricsCollector
from ..agents.api_writer_agent import ApiWriterAgent


class PerformanceOptimizer:
    """Analyze metrics and suggest bid or budget adjustments."""

    def __init__(self, api_writer: ApiWriterAgent | None = None) -> None:
        self.collector = MetricsCollector()
        self.api_writer = api_writer or ApiWriterAgent()

    def analyze(self, metrics: Iterable[Mapping[str, Any]]) -> Mapping[str, float]:
        for m in metrics:
            self.collector.add(
                impressions=int(m.get("impressions", 0)),
                clicks=int(m.get("clicks", 0)),
                cost=float(m.get("cost", 0.0)),
                conversions=int(m.get("conversions", 0)),
                revenue=float(m.get("revenue", 0.0)),
                returning_customers=int(m.get("returning_customers", 0)),
            )
        return self.collector.collect()

    def suggest_adjustments(self, kpis: Mapping[str, float]) -> str:
        bid = "increase bids" if kpis.get("CTR", 0.0) < 0.02 else "maintain bids"
        roas = kpis.get("ROAS", 0.0)
        if roas < 1.0:
            budget = "decrease budget"
        elif roas > 2.0:
            budget = "increase budget"
        else:
            budget = "maintain budget"
        return f"Bid suggestion: {bid}; Budget suggestion: {budget}"

    def analyze_and_forward(self, metrics: Iterable[Mapping[str, Any]]) -> str:
        kpis = self.analyze(metrics)
        suggestion = self.suggest_adjustments(kpis)
        return self.api_writer.run(suggestion)
