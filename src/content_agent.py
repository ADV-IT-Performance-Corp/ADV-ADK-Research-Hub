from base_agent import BaseAgent


class ContentAgent(BaseAgent):
    """Example agent that generates short content snippets."""

    def __init__(self) -> None:
        super().__init__("ContentAgent")

    def run(self, topic: str) -> str:
        snippet = f"Generated content for: {topic}"
        return f"{self.name}: {snippet}"
