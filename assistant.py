"""Async marketing assistant orchestrating planner->creative->budgeter->api_writer."""

from __future__ import annotations

import asyncio
from typing import Any, Dict

from o3research.core.async_event_bus import AsyncEventBus
from o3research.core.semantic_cache import SemanticCache
from o3research.agents.marketing_assistant.planner import PlannerAgent
from o3research.marketing import CreativeAgent, Budgeter, push_campaign


# Shared objects
_event_bus = AsyncEventBus()
_cache = SemanticCache()
_planner = PlannerAgent()
_creative = CreativeAgent()
_budgeter = Budgeter()


async def _handle_plan(product: str) -> None:
    """Generate plan then trigger creative stage."""
    plan = _planner.run(product)
    _cache.set("plan", plan)
    await _event_bus.publish("creative", product)


async def _handle_creative(product: str) -> None:
    """Generate ad copy then trigger budget stage."""
    copy = _creative.run(product, "growth marketer")
    _cache.set("creative", copy)
    sample = {
        "search": {
            "metrics": {
                "impressions": 1000,
                "clicks": 100,
                "cost": 100.0,
                "conversions": 10,
                "revenue": 200.0,
            }
        },
        "social": {
            "metrics": {
                "impressions": 500,
                "clicks": 50,
                "cost": 50.0,
                "conversions": 5,
                "revenue": 80.0,
            }
        },
    }
    await _event_bus.publish("budget", sample)


async def _handle_budget(plans: Dict[str, Dict[str, Any]]) -> None:
    """Allocate spend and push campaign."""
    allocation = _budgeter.allocate(plans)
    _cache.set("budget", str(allocation))
    campaign_id = push_campaign({"name": "Async Campaign"})
    _cache.set("campaign", campaign_id)
    summary = (
        f"{_cache.get('plan')}\n"
        f"{_cache.get('creative')}\n"
        f"Budget allocations: {allocation}\n"
        f"Pushed campaign: {campaign_id}"
    )
    _cache.set("summary", summary)


def _setup() -> None:
    _event_bus.subscribe("plan", _handle_plan)
    _event_bus.subscribe("creative", _handle_creative)
    _event_bus.subscribe("budget", _handle_budget)


async def run_campaign(product: str) -> str:
    """Run full workflow and return campaign summary."""
    _setup()
    await _event_bus.publish("plan", product)
    return _cache.get("summary") or ""


if __name__ == "__main__":  # pragma: no cover
    result = asyncio.run(run_campaign("demo product"))
    print(result)
