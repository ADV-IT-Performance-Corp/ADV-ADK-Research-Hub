from google.adk import Agent


class AnalyticsAgent(Agent):
    """Agent that reports campaign KPIs."""

    def __init__(self) -> None:
        super().__init__(name="AnalyticsAgent")

    def run(self, data: str) -> str:
        return f"{self.name} analyzed data: {data}"
