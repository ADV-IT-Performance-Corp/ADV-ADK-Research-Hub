from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "4.0.0"


class ResearchAgent(Agent):
    """Example agent that returns a research summary."""

    def __init__(self) -> None:
        super().__init__(name="ResearchAgent")

    def run(self, query: str) -> str:
        start_run(self.name)
        try:
            return f"{self.name} researched: {query}"
        finally:
            finish_run(self.name)


if __name__ == "__main__":
    agent = ResearchAgent()
    print(agent.run("market trends"))
