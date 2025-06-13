from google.adk import Agent
from o3research.lifecycle import finish_run, start_run

__version__ = "4.0.0"


class CampaignAgent(Agent):
    """Example agent that plans a marketing campaign."""

    def __init__(self) -> None:
        super().__init__(name="CampaignAgent")

    def run(self, product: str) -> str:
        start_run(self.name)
        try:
            return f"{self.name} plans a campaign for {product}"
        finally:
            finish_run(self.name)


if __name__ == "__main__":
    agent = CampaignAgent()
    print(agent.run("new SaaS"))
