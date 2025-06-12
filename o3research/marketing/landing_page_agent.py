import time
from google.adk import Agent
from o3research.lifecycle import finish_run, start_run
from .prompt_observability import record_prompt


class LandingPageAgent(Agent):
    """Create a short landing page outline."""

    def __init__(self) -> None:
        super().__init__(name="LandingPageAgent")

    def run(self, product: str, value_prop: str) -> str:  # type: ignore[override]
        """Return landing page headline and bullet points."""
        start_run(self.name)
        start = time.perf_counter()
        ref = "docs/performance_marketing/landing_page_content.md lines 8-18"
        lines = [
            f"Landing page for {product}:",
            f"Headline: Experience {product} today",
            f"Subheadline: {value_prop}",
            "Key points:",
            "- Clear benefits",
            "- Social proof",
            "- Single call to action",
            f"(See {ref})",
        ]
        result = "\n".join(lines)
        latency = time.perf_counter() - start
        record_prompt("landing_page", self.name, result, timing=latency, cost=0.0)
        finish_run(self.name)
        return result
