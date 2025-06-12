from google.adk import Agent

__version__ = "3.5.9"
from typing import Dict, Any


class AbTestingAgent(Agent):
    """Agent that selects the best performing variant."""

    def __init__(self) -> None:
        super().__init__(name="AbTestingAgent")

    def run(self, variants: Dict[str, Dict[str, Any]]) -> str:
        """Return the variant with the highest conversion rate.

        Each variant should provide at least ``clicks`` and ``conversions`` keys.
        Conversion rate is computed as conversions / clicks. A rate of 0 is used
        if clicks is 0.
        """
        best_variant = None
        best_rate = -1.0
        for name, metrics in variants.items():
            clicks = metrics.get("clicks", 0)
            conversions = metrics.get("conversions", 0)
            rate = conversions / clicks if clicks else 0.0
            if rate > best_rate:
                best_rate = rate
                best_variant = name
        return f"{self.name} selected {best_variant}"
