from google.adk import Agent


class EngagementAgent(Agent):
    """Agent that handles customer engagement tasks."""

    def __init__(self) -> None:
        super().__init__(name="EngagementAgent")

    def run(self, lead: str) -> str:
        return f"{self.name} nurtures lead: {lead}"
