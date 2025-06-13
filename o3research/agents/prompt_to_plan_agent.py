from google.adk import Agent
from ..core.telemetry import log_prompt
from o3research.lifecycle import finish_run, start_run

__version__ = "4.0.0"


class PromptToPlanAgent(Agent):
    """Convert a text prompt into an actionable plan."""

    def __init__(self) -> None:
        super().__init__(name="PromptToPlanAgent")

    def run(self, prompt: str) -> str:  # type: ignore[override]
        start_run(self.name)
        try:
            steps = [
                f"Action plan for: {prompt}",
                "- Clarify objectives",
                "- Generate creative ideas",
                "- Assign tasks to teams",
                "- Define success metrics",
            ]
            plan = "\n".join(steps)
            log_prompt("prompt_to_plan", self.name, len(plan.split()))
            return plan
        finally:
            finish_run(self.name)


__all__ = ["PromptToPlanAgent"]
