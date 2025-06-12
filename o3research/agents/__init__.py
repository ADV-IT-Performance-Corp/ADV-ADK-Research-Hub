"""Agent package initialization."""

__version__ = "3.5.9"

from .agent_registry import register_agent, get_agent, clear_registry
from .sample_agent import EchoAgent
from .research_agent import ResearchAgent
from .marketing_assistant import (
    ContentAgent,
    CampaignAgent,
    EngagementAgent,
    OptimizationAgent,
    AnalyticsAgent,
    ConfigAgent,
    GovernanceAgent,
    AbTestingAgent,
)
from .prompt_to_plan_agent import PromptToPlanAgent
from .api_writer_agent import ApiWriterAgent

__all__ = [
    "register_agent",
    "get_agent",
    "clear_registry",
    "EchoAgent",
    "ResearchAgent",
    "ContentAgent",
    "CampaignAgent",
    "EngagementAgent",
    "OptimizationAgent",
    "AnalyticsAgent",
    "ConfigAgent",
    "GovernanceAgent",
    "AbTestingAgent",
    "PromptToPlanAgent",
    "ApiWriterAgent",
]
