from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "4.0.0"


class OptimizationAgent(Agent):
    """Agent that tunes campaign parameters based on metrics."""

    def __init__(self) -> None:
        super().__init__(name="OptimizationAgent")

    def run(self, metric: str) -> str:
        start_run(self.name)
        try:
            return f"{self.name} optimizes for {metric}"
        finally:
            finish_run(self.name)
