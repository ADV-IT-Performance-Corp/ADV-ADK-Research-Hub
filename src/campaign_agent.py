from base_agent import BaseAgent


class CampaignAgent(BaseAgent):
    """Agent for planning basic campaign steps."""

    def __init__(self) -> None:
        super().__init__("CampaignAgent")

    def run(self, product: str) -> str:
        """Return a simple campaign plan summary."""
        return (
            f"{self.name} drafted a campaign plan for '{product}', "
            "covering channels and timing."
        )
