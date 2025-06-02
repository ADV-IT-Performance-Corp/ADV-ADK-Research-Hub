from typing import Callable, Dict, List


class MetricsCollector:
    """Aggregate metrics from multiple sources."""

    def __init__(self) -> None:
        self.sources: List[Callable[[], Dict[str, float]]] = []

    def add_source(self, source: Callable[[], Dict[str, float]]) -> None:
        self.sources.append(source)

    def collect(self) -> Dict[str, float]:
        aggregated = {"impressions": 0.0, "clicks": 0.0, "conversions": 0.0}
        for src in self.sources:
            data = src()
            for key in aggregated:
                aggregated[key] += data.get(key, 0.0)
        return aggregated
