from base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    """Example agent that synthesizes research notes."""

    def __init__(self) -> None:
        super().__init__("ResearchAgent")

    def run(self, query: str) -> str:
        # Placeholder logic for demonstration purposes
        notes = f"Researching: {query}"
        return f"{self.name}: {notes}"
