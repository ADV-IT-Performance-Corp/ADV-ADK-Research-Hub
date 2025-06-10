from ..core.base_agent import BaseAgent
from ..core.telemetry import log_prompt


class CreativeAgent(BaseAgent):
    """Provide short creative ad suggestions."""

    def __init__(self) -> None:
        super().__init__(name="CreativeAgent")

    def run(self, product: str, audience: str) -> str:  # type: ignore[override]
        """Return short ad copy suggestions for *product* targeting *audience*."""
        suggestions = [
            f"Unlock productivity with {product} for {audience}",
            f"{audience.capitalize()} excel faster using {product}",
            f"Try {product} today and see results quickly",
        ]
        lines = ["Creative suggestions:"] + [f"- {s}" for s in suggestions]
        result = "\n".join(lines)
        log_prompt("creative_suggestions", self.name, len(result.split()))
        return result
