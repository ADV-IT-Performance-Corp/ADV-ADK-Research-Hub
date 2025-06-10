import sys
import importlib
import types
import unittest


class TestConfigAgentWithDummyYAML(unittest.TestCase):
    def test_config_agent_with_dummy_yaml(self):
        original_yaml = sys.modules.get("yaml")
        dummy_yaml = types.ModuleType("yaml")
        dummy_yaml.safe_load = lambda data: {"dummy": True}
        sys.modules["yaml"] = dummy_yaml

        try:
            import o3research.agents.config_agent as config_agent

            importlib.reload(config_agent)
            ConfigAgent = config_agent.ConfigAgent

            agent = ConfigAgent()
            settings = agent.load_settings()
            self.assertIsInstance(settings, dict)
            result = agent.run("")
            self.assertTrue(result.startswith("ConfigAgent loaded"))
        finally:
            if original_yaml is not None:
                sys.modules["yaml"] = original_yaml
            else:
                sys.modules.pop("yaml", None)
            importlib.reload(config_agent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
