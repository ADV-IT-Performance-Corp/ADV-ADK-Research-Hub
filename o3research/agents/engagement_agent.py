from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "3.5.10"


class EngagementAgent(Agent):
    """Agent that handles customer engagement tasks."""

    def __init__(self) -> None:
        super().__init__(name="EngagementAgent")

    def run(self, lead: str) -> str:
        start_run(self.name)
        try:
            return f"{self.name} nurtures lead: {lead}"
        finally:
            finish_run(self.name)
