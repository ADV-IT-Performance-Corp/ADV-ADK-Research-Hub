from __future__ import annotations

from typing import Mapping, Any

from google.adk import Agent

__version__ = "3.5.10"


class LeadScoringAgent(Agent):
    """Assign a basic score to a lead record."""

    def __init__(self) -> None:
        super().__init__(name="LeadScoringAgent")

    def run(self, lead: Mapping[str, Any]) -> str:  # type: ignore[override]
        """Return a score for *lead* based on simple heuristics."""
        score = 50
        if lead.get("industry") == "technology":
            score += 20
        if float(lead.get("annual_revenue", 0)) > 1_000_000:
            score += 30
        return f"{self.name} scored {lead.get('name', 'lead')} {score}"
