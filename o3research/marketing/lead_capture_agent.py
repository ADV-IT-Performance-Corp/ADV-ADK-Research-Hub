import time
from google.adk import Agent
from .prompt_observability import record_prompt


class LeadCaptureAgent(Agent):
    """Suggest a basic lead capture workflow."""

    def __init__(self) -> None:
        super().__init__(name="LeadCaptureAgent")

    def run(self, method: str) -> str:  # type: ignore[override]
        """Return steps for capturing leads using *method*."""
        start = time.perf_counter()
        ref = "docs/performance_marketing/lead_capture_techniques.md lines 6-14"
        lines = [
            f"Lead capture via {method}:",
            "- Display short form",
            "- Use progressive profiling",
            "- Confirm email and tag user",
            f"(See {ref})",
        ]
        result = "\n".join(lines)
        latency = time.perf_counter() - start
        record_prompt("lead_capture", self.name, result, timing=latency, cost=0.0)
        return result
