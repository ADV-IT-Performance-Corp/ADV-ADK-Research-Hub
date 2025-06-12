from google.adk import Agent


class OptimizationAgent(Agent):
    """Agent that tunes campaign parameters based on metrics."""

    def __init__(self) -> None:
        super().__init__(name="OptimizationAgent")

    def run(self, metric: str) -> str:
        return f"{self.name} optimizes for {metric}"
