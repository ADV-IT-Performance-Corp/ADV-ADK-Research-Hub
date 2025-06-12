from google.adk import Agent


class ResearchAgent(Agent):
    """Example agent that returns a research summary."""

    def __init__(self) -> None:
        super().__init__(name="ResearchAgent")

    def run(self, query: str) -> str:
        return f"{self.name} researched: {query}"


if __name__ == "__main__":
    agent = ResearchAgent()
    print(agent.run("market trends"))
