from ..core.base_agent import BaseAgent


class CreativePromptAgent(BaseAgent):
    """Generate short ad copy variants for a target persona."""

    def __init__(self) -> None:
        super().__init__(name="CreativePromptAgent")

    def run(self, product: str, persona: str) -> str:  # type: ignore[override]
        """Return multiple ad copy lines referencing neuromarketing tactics."""
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
        return "\n".join(lines)
