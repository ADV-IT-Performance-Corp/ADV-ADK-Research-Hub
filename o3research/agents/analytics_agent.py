from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "3.5.10"


class AnalyticsAgent(Agent):
    """Agent that reports campaign KPIs."""

    def __init__(self) -> None:
        super().__init__(name="AnalyticsAgent")

    def run(self, data: str) -> str:
        start_run(self.name)
        try:
            return f"{self.name} analyzed data: {data}"
        finally:
            finish_run(self.name)
