from google.adk import Agent
from ..core.telemetry import log_prompt

__version__ = "3.5.10"


class PromptToPlanAgent(Agent):
    """Convert a text prompt into an actionable plan."""

    def __init__(self) -> None:
        super().__init__(name="PromptToPlanAgent")

    def run(self, prompt: str) -> str:  # type: ignore[override]
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


__all__ = ["PromptToPlanAgent"]
