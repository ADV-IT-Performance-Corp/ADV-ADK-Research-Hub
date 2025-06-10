from ..core.base_agent import BaseAgent


class ApiWriterAgent(BaseAgent):
    """Agent that sends suggestions to an external API."""

    def __init__(self) -> None:
        super().__init__(name="ApiWriterAgent")

    def run(self, message: str) -> str:
        """Pretend to send *message* to an API and return confirmation."""
        return f"{self.name} sent: {message}"
