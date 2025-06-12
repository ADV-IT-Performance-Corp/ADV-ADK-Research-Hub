from google.adk import Agent

__version__ = "3.5.9"


class ApiWriterAgent(Agent):
    """Agent that sends suggestions to an external API."""

    def __init__(self) -> None:
        super().__init__(name="ApiWriterAgent")

    def run(self, message: str) -> str:
        """Pretend to send *message* to an API and return confirmation."""
        return f"{self.name} sent: {message}"
