from core.base_agent import BaseAgent


class ContentAgent(BaseAgent):
    """Example agent that suggests content ideas."""

    def __init__(self) -> None:
        super().__init__(name="ContentAgent")

    def run(self, topic: str) -> str:
        return f"{self.name} suggests a blog post about '{topic}'"


if __name__ == "__main__":
    agent = ContentAgent()
    print(agent.run("AI marketing"))
