"""Agent for extracting trending keywords from CSV data."""

from __future__ import annotations

import csv
from io import StringIO
from typing import Dict, List

from google.adk import Agent


class KeywordMapperAgent(Agent):
    """Parse keyword volume data and return the top terms."""

    def __init__(self) -> None:
        super().__init__(name="KeywordMapperAgent")

    @staticmethod
    def parse_csv(data: str) -> Dict[str, int]:
        """Return mapping of keyword to volume from CSV ``data``."""
        reader = csv.DictReader(StringIO(data))
        mapping: Dict[str, int] = {}
        for row in reader:
            kw = (row.get("keyword") or "").strip()
            vol = int(row.get("volume", 0))
            if kw:
                mapping[kw] = vol
        return mapping

    @staticmethod
    def top_keywords(mapping: Dict[str, int], limit: int = 5) -> List[str]:
        """Return ``limit`` keywords sorted by descending volume."""
        sorted_items = sorted(mapping.items(), key=lambda i: i[1], reverse=True)
        return [k for k, _ in sorted_items[:limit]]

    def run(self, data: str) -> str:  # type: ignore[override]
        mapping = self.parse_csv(data)
        keywords = self.top_keywords(mapping)
        return "Top keywords: " + ", ".join(keywords)


__all__ = ["KeywordMapperAgent"]
