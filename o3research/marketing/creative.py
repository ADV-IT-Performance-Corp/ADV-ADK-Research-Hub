from ..core.base_agent import BaseAgent
import time
from ..core.telemetry import log_prompt


class CreativeAgent(BaseAgent):
    """Provide short creative ad suggestions."""

    def __init__(self) -> None:
        super().__init__(name="CreativeAgent")

    def run(self, product: str, audience: str) -> str:  # type: ignore[override]
        """Return short ad copy suggestions for *product* targeting *audience*."""
        start = time.perf_counter()
        suggestions = [
            f"Unlock productivity with {product} for {audience}",
            f"{audience.capitalize()} excel faster using {product}",
            f"Try {product} today and see results quickly",
        ]
        lines = ["Creative suggestions:"] + [f"- {s}" for s in suggestions]
        result = "\n".join(lines)
        latency = time.perf_counter() - start
        log_prompt(
            "creative_suggestions",
            self.name,
            len(result.split()),
            timing=latency,
            cost=0.0,
        )
        return result
