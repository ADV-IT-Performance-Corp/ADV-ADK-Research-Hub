from google.adk import Agent
from .agents.sample_agent import EchoAgent
from .agents.research_agent import ResearchAgent
from .core.task_flow import TaskFlow
from .core.executor import Executor
from .core.prompt_gen import get_prompt, DEFAULT_PROMPT
from .core.prompt_manager import PromptManager
from .core.context import Context

import pathlib

_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
with (_BASE_DIR / "VERSION").open() as vf:
    __version__ = vf.read().strip()


__all__ = [
    "Agent",
    "EchoAgent",
    "ResearchAgent",
    "TaskFlow",
    "Executor",
    "get_prompt",
    "DEFAULT_PROMPT",
    "PromptManager",
    "Context",
    "__version__",
]
