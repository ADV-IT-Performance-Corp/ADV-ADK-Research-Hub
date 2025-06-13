from pathlib import Path

__version__ = "4.0.0"
from typing import Any, Dict

import yaml
from google.adk import Agent
from o3research.lifecycle import finish_run, start_run
from pydantic import ConfigDict


class ConfigAgent(Agent):
    model_config = ConfigDict(extra="allow")
    """Agent that applies configuration updates."""

    def __init__(self, settings_file: str = "config/settings.yaml") -> None:
        super().__init__(name="ConfigAgent")
        self.settings_file = Path(settings_file)

    def load_settings(self) -> Dict[str, Any]:
        if not self.settings_file.exists():
            return {}
        return yaml.safe_load(self.settings_file.read_text())

    def run(self, _: str) -> str:
        start_run(self.name)
        try:
            settings = self.load_settings()
            return f"{self.name} loaded {len(settings)} settings"
        finally:
            finish_run(self.name)
