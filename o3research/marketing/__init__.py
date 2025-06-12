"""Marketing agents package."""

from .google_ads_agent import GoogleAdsCampaignAgent
from .meta_ads_agent import MetaAdsAgent
from .budget_allocator import BudgetAllocatorAgent
from .budgeter import Budgeter
from .funnel_planner import FunnelPlannerAgent
from .creative_prompt_agent import CreativePromptAgent
from .creative import CreativeAgent
from .landing_page_agent import LandingPageAgent
from .lead_capture_agent import LeadCaptureAgent
from .optimizer import PerformanceOptimizer
from .api_writer import push_campaign

__all__ = [
    "GoogleAdsCampaignAgent",
    "MetaAdsAgent",
    "BudgetAllocatorAgent",
    "Budgeter",
    "FunnelPlannerAgent",
    "CreativePromptAgent",
    "CreativeAgent",
    "LandingPageAgent",
    "LeadCaptureAgent",
    "PerformanceOptimizer",
    "push_campaign",
]
