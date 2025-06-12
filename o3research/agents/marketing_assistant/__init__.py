"""Convenience imports for marketing assistant roles."""

__version__ = "3.5.10"

from ..research_agent import ResearchAgent
from ..content_agent import ContentAgent
from ..campaign_agent import CampaignAgent
from ..engagement_agent import EngagementAgent
from ..optimization_agent import OptimizationAgent
from ..analytics_agent import AnalyticsAgent
from ..config_agent import ConfigAgent
from ..governance_agent import GovernanceAgent
from ..ab_testing_agent import AbTestingAgent
from .planner import PlannerAgent

__all__ = [
    "ResearchAgent",
    "ContentAgent",
    "CampaignAgent",
    "EngagementAgent",
    "OptimizationAgent",
    "AnalyticsAgent",
    "ConfigAgent",
    "GovernanceAgent",
    "AbTestingAgent",
    "PlannerAgent",
]
