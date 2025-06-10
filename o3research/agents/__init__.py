"""Agent package initialization."""

from .agent_registry import register_agent, get_agent, clear_registry
from .sample_agent import EchoAgent
from .research_agent import ResearchAgent

__all__ = [
    "register_agent",
    "get_agent",
    "clear_registry",
    "EchoAgent",
    "ResearchAgent",
]
