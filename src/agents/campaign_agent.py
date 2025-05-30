from core.base_agent import BaseAgent


class CampaignAgent(BaseAgent):
    """Example agent that plans a marketing campaign."""

    def __init__(self) -> None:
        super().__init__(name="CampaignAgent")

    def run(self, product: str) -> str:
        return f"{self.name} plans a campaign for {product}"


if __name__ == "__main__":
    agent = CampaignAgent()
    print(agent.run("new SaaS"))
