from ..core.base_agent import BaseAgent
from .prompt_observability import record_prompt


class MetaAdsAgent(BaseAgent):
    """Generate a Meta Advantage+ style campaign plan."""

    def __init__(self) -> None:
        super().__init__(name="MetaAdsAgent")

    def run(self, offer: str) -> str:
        """Return a simplified Advantage+ ad strategy."""
        summary_ref = "docs/performance_marketing/meta_ai_strategy.md lines 8-11"
        plan = (
            f"Advantage+ campaign for {offer}:\n"
            "- Leverage dynamic creative optimization to mix ad assets\n"
            "- Enable audience expansion to find high-value buyers\n"
            f"(See {summary_ref})"
        )
        record_prompt("meta_ads_plan", self.name, plan)
        return plan


if __name__ == "__main__":  # pragma: no cover
    agent = MetaAdsAgent()
    print(agent.run("new product"))
