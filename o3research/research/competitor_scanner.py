"""Agent for scraping basic data from competitor websites."""

from __future__ import annotations

import re
from urllib import request

from google.adk import Agent


class CompetitorScannerAgent(Agent):
    """Scrape the page title from a competitor URL."""

    def __init__(self) -> None:
        super().__init__(name="CompetitorScannerAgent")

    def fetch_page(self, url: str) -> str:
        """Retrieve the raw HTML for *url*."""
        with request.urlopen(url) as resp:  # pragma: no cover - network
            return resp.read().decode("utf-8", errors="ignore")

    @staticmethod
    def extract_title(html: str) -> str:
        """Return the page ``<title>`` text from ``html`` if present."""
        match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else "unknown"

    def run(self, url: str) -> str:  # type: ignore[override]
        html = self.fetch_page(url)
        title = self.extract_title(html)
        return f"Competitor page title: {title}"


__all__ = ["CompetitorScannerAgent"]
