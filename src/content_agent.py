from base_agent import BaseAgent


class ContentAgent(BaseAgent):
    """Agent responsible for generating simple content snippets."""

    def __init__(self) -> None:
        super().__init__("ContentAgent")

    def run(self, topic: str) -> str:
        """Return a mock content outline."""
        return f"{self.name} produced a short post about '{topic}'."
