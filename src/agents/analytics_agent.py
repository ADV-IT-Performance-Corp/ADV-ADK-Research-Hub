from ..core.base_agent import BaseAgent


class AnalyticsAgent(BaseAgent):
    """Agent that reports campaign KPIs."""

    def __init__(self) -> None:
        super().__init__(name="AnalyticsAgent")

    def run(self, data: str) -> str:
        return f"{self.name} analyzed data: {data}"
