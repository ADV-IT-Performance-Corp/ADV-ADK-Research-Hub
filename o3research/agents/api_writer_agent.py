from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "4.0.0"


class ApiWriterAgent(Agent):
    """Agent that sends suggestions to an external API."""

    def __init__(self) -> None:
        super().__init__(name="ApiWriterAgent")

    def run(self, message: str) -> str:
        """Pretend to send *message* to an API and return confirmation."""
        start_run(self.name)
        try:
            return f"{self.name} sent: {message}"
        finally:
            finish_run(self.name)
