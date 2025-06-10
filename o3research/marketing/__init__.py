"""Marketing agents package."""

from .google_ads_agent import GoogleAdsCampaignAgent
from .meta_ads_agent import MetaAdsAgent
from .budget_allocator import BudgetAllocatorAgent
from .funnel_planner import FunnelPlannerAgent
from .creative_prompt_agent import CreativePromptAgent

__all__ = [
    "GoogleAdsCampaignAgent",
    "MetaAdsAgent",
    "BudgetAllocatorAgent",
    "FunnelPlannerAgent",
    "CreativePromptAgent",
]
