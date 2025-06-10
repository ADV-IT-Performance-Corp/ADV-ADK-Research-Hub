import time
from ..core.base_agent import BaseAgent
from .prompt_observability import record_prompt


class CreativePromptAgent(BaseAgent):
    """Generate short ad copy variants for a target persona."""

    def __init__(self) -> None:
        super().__init__(name="CreativePromptAgent")

    def run(self, product: str, persona: str) -> str:  # type: ignore[override]
        """Return multiple ad copy lines referencing neuromarketing tactics."""
        start = time.perf_counter()
        ref = "docs/performance_marketing/neurogym_neuromarketing.md lines 14-23"
        variants = [
            f"Imagine if {persona} used {product} and felt unstoppable. Act now!",
            (
                f"{persona.capitalize()}, avoid the pain of slow results. "
                f"{product} unlocks new gains."
            ),
            f"See your vision come alive with {product}, {persona}!",
        ]
        lines = ["Ad copy variants:"] + [f"- {v}" for v in variants] + [f"(See {ref})"]
        result = "\n".join(lines)
        latency = time.perf_counter() - start
        record_prompt(
            "creative_prompt_variants",
            self.name,
            result,
            timing=latency,
            cost=0.0,
        )
        return result
