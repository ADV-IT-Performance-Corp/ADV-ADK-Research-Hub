from base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Example agent that returns a simple research note."""

    def __init__(self, name: str = "ResearchAgent") -> None:
        super().__init__(name)

    def run(self, query: str) -> str:
        return f"{self.name} researched: {query}"
