try:
    from .base_agent import BaseAgent
except ImportError:  # Fallback for running as a script
    from base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Basic research agent stub."""

    def __init__(self, name: str = "ResearchAgent") -> None:
        super().__init__(name)

    def run(self, query: str) -> str:
        """Return a placeholder research result."""
        return f"{self.name} results for '{query}'"


if __name__ == "__main__":
    agent = ResearchAgent()
    print(agent.run("market trends"))
