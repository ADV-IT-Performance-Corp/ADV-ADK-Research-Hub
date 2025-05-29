from base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Agent for gathering competitive intelligence."""

    def __init__(self) -> None:
        super().__init__("ResearchAgent")

    def run(self, query: str) -> str:
        """Return a stubbed research summary."""
        return f"{self.name} researched '{query}'" \
               " and compiled relevant insights."
