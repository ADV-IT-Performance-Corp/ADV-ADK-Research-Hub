from __future__ import annotations

import pathlib

_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
with (_BASE_DIR / "VERSION").open() as version_file:
    __version__ = version_file.read().strip()

__all__ = ["__version__"]


def __getattr__(name: str):
    """Dynamically import select attributes on demand."""
    if name == "Agent":
        from google.adk import Agent

        return Agent
    if name == "EchoAgent":
        from .agents.sample_agent import EchoAgent

        return EchoAgent
    if name == "ResearchAgent":
        from .agents.research_agent import ResearchAgent

        return ResearchAgent
    if name == "TaskFlow":
        from .core.task_flow import TaskFlow

        return TaskFlow
    if name == "Executor":
        from .core.executor import Executor

        return Executor
    if name == "get_prompt":
        from .core.prompt_gen import get_prompt

        return get_prompt
    if name == "DEFAULT_PROMPT":
        from .core.prompt_gen import DEFAULT_PROMPT

        return DEFAULT_PROMPT
    if name == "PromptManager":
        from .core.prompt_manager import PromptManager

        return PromptManager
    if name == "Context":
        from .core.context import Context

        return Context
    raise AttributeError(name)
