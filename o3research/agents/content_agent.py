from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "3.5.10"


class ContentAgent(Agent):
    """Example agent that suggests content ideas."""

    def __init__(self) -> None:
        super().__init__(name="ContentAgent")

    def run(self, topic: str) -> str:
        start_run(self.name)
        try:
            return f"{self.name} suggests a blog post about '{topic}'"
        finally:
            finish_run(self.name)


if __name__ == "__main__":
    agent = ContentAgent()
    print(agent.run("AI marketing"))
