"""Expose core classes and project version."""

from pathlib import Path

from .core.base_agent import BaseAgent
from .agents.sample_agent import EchoAgent
from .agents.research_agent import ResearchAgent

_root = Path(__file__).resolve().parents[1]
__version__ = (_root / "VERSION").read_text().strip()

__all__ = ["BaseAgent", "EchoAgent", "ResearchAgent"]
