from .core.base_agent import BaseAgent
from .agents.sample_agent import EchoAgent
from .agents.research_agent import ResearchAgent
from .agents.ab_testing_agent import ABTestingAgent
from .integrations import GoogleAdsClient, MetaAdsClient

import pathlib

_BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
with (_BASE_DIR / "VERSION").open() as vf:
    __version__ = vf.read().strip()


__all__ = [
    "BaseAgent",
    "EchoAgent",
    "ResearchAgent",
    "ABTestingAgent",
    "GoogleAdsClient",
    "MetaAdsClient",
    "__version__",
]
