"""Agent package initialization."""

from __future__ import annotations

__version__ = "4.0.0"

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
    "__version__",
]


def __getattr__(name: str):
    if name == "register_agent":
        from .agent_registry import register_agent

        return register_agent
    if name == "get_agent":
        from .agent_registry import get_agent

        return get_agent
    if name == "clear_registry":
        from .agent_registry import clear_registry

        return clear_registry
    if name == "EchoAgent":
        from .sample_agent import EchoAgent

        return EchoAgent
    if name == "ResearchAgent":
        from .research_agent import ResearchAgent

        return ResearchAgent
    if name == "ContentAgent":
        from .marketing_assistant import ContentAgent

        return ContentAgent
    if name == "CampaignAgent":
        from .marketing_assistant import CampaignAgent

        return CampaignAgent
    if name == "EngagementAgent":
        from .marketing_assistant import EngagementAgent

        return EngagementAgent
    if name == "OptimizationAgent":
        from .marketing_assistant import OptimizationAgent

        return OptimizationAgent
    if name == "AnalyticsAgent":
        from .marketing_assistant import AnalyticsAgent

        return AnalyticsAgent
    if name == "ConfigAgent":
        from .marketing_assistant import ConfigAgent

        return ConfigAgent
    if name == "GovernanceAgent":
        from .marketing_assistant import GovernanceAgent

        return GovernanceAgent
    if name == "AbTestingAgent":
        from .marketing_assistant import AbTestingAgent

        return AbTestingAgent
    if name == "PromptToPlanAgent":
        from .prompt_to_plan_agent import PromptToPlanAgent

        return PromptToPlanAgent
    if name == "ApiWriterAgent":
        from .api_writer_agent import ApiWriterAgent

        return ApiWriterAgent
    raise AttributeError(name)


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
