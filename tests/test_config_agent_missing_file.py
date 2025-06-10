import unittest
from tempfile import TemporaryDirectory
from pathlib import Path

from o3research.agents.config_agent import ConfigAgent


class TestConfigAgentMissingFile(unittest.TestCase):
    def test_load_settings_missing_file(self) -> None:
        with TemporaryDirectory() as tmpdir:
            missing_path = Path(tmpdir) / "nonexistent.yaml"
            agent = ConfigAgent(settings_file=str(missing_path))
            self.assertEqual(agent.load_settings(), {})
            self.assertEqual(agent.run(""), "ConfigAgent loaded 0 settings")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
