from pathlib import Path
from .core.base_agent import BaseAgent
from .agents.sample_agent import EchoAgent
from .agents.research_agent import ResearchAgent

# Expose library version from VERSION file
_version_file = Path(__file__).resolve().parent.parent / "VERSION"
__version__ = _version_file.read_text().strip() if _version_file.exists() else "0.0.0"

__all__ = ["BaseAgent", "EchoAgent", "ResearchAgent"]
