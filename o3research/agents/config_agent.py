from pathlib import Path
from typing import Any, Dict

import yaml
from ..core.base_agent import BaseAgent


class ConfigAgent(BaseAgent):
    """Agent that applies configuration updates."""

    def __init__(self, settings_file: str = "config/settings.yaml") -> None:
        super().__init__(name="ConfigAgent")
        self.settings_file = Path(settings_file)

    def load_settings(self) -> Dict[str, Any]:
        if not self.settings_file.exists():
            return {}
        return yaml.safe_load(self.settings_file.read_text())

    def run(self, _: str) -> str:
        settings = self.load_settings()
        return f"{self.name} loaded {len(settings)} settings"
