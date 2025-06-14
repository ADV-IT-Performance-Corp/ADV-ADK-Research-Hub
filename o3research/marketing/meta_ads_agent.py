import time
from google.adk import Agent
from o3research.lifecycle import finish_run, start_run
from .prompt_observability import record_prompt


class MetaAdsAgent(Agent):
    """Generate a Meta Advantage+ style campaign plan."""

    def __init__(self) -> None:
        super().__init__(name="MetaAdsAgent")

    def run(self, offer: str) -> str:
        """Return a simplified Advantage+ ad strategy."""
        start_run(self.name)
        try:
            start = time.perf_counter()
            summary_ref = "docs/performance_marketing/meta_ai_strategy.md lines 8-11"
            plan = (
                f"Advantage+ campaign for {offer}:\n"
                "- Leverage dynamic creative optimization to mix ad assets\n"
                "- Enable audience expansion to find high-value buyers\n"
                f"(See {summary_ref})"
            )
            latency = time.perf_counter() - start
            record_prompt("meta_ads_plan", self.name, plan, timing=latency, cost=0.0)
            return plan
        finally:
            finish_run(self.name)


if __name__ == "__main__":  # pragma: no cover
    agent = MetaAdsAgent()
    print(agent.run("new product"))
