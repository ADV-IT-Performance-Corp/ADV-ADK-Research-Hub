from ..core.base_agent import BaseAgent
from ..core.metrics import MetricsCollector


class ABTestingAgent(BaseAgent):
    """Selects the best performing variant based on collected metrics."""

    def __init__(self) -> None:
        super().__init__(name="ABTestingAgent")
        self.collector = MetricsCollector()

    def run(self, variants):
        metrics = self.collector.collect()
        # Placeholder: pick the first variant
        return variants[0], metrics
