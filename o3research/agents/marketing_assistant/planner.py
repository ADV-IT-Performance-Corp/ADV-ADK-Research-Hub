from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "3.5.10"
from ...core.telemetry import log_prompt


class PlannerAgent(Agent):
    """Create a basic multi-channel marketing campaign plan."""

    def __init__(self) -> None:
        super().__init__(name="PlannerAgent")

    def run(self, prompt: str) -> str:  # type: ignore[override]
        """Return a simple campaign plan for *prompt*."""
        start_run(self.name)
        try:
            plan_lines = [
                f"Campaign plan for {prompt}:",
                "- Research target audience and key pain points",
                "- Develop messaging themes and creative assets",
                "- Launch across search, social, and email channels",
                "- Measure KPIs: impressions, clicks, and conversions",
            ]
            plan = "\n".join(plan_lines)
            log_prompt("marketing_planner", self.name, len(plan.split()))
            return plan
        finally:
            finish_run(self.name)
