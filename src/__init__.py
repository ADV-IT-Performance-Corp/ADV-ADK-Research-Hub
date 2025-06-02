from pathlib import Path
from .core.base_agent import BaseAgent
from .agents.sample_agent import EchoAgent
from .agents.research_agent import ResearchAgent

_version_path = Path(__file__).resolve().parent.parent / "VERSION"
__version__ = _version_path.read_text().strip()

__all__ = ["BaseAgent", "EchoAgent", "ResearchAgent", "__version__"]
