from ..core.base_agent import BaseAgent


class GoogleAdsCampaignAgent(BaseAgent):
    """Generate a simple Google Ads campaign plan."""

    def __init__(self) -> None:
        super().__init__(name="GoogleAdsCampaignAgent")

    def run(self, offer: str) -> str:
        """Return a basic campaign plan for the given product or offer."""
        summary_ref = "docs/performance_marketing/google_insights_summary.md lines 8-21"
        plan = (
            f"Plan for {offer}:\n"
            "- Channels: Search, Display\n"
            "- Keywords: focus on smart bidding and audience segments\n"
            "- Ads: enable cross-channel attribution\n"
            f"(See {summary_ref})"
        )
        return plan


if __name__ == "__main__":  # pragma: no cover
    agent = GoogleAdsCampaignAgent()
    print(agent.run("new SaaS"))
