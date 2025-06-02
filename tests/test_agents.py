import unittest
from src.agents.research_agent import ResearchAgent
try:
    from src.agents.config_agent import ConfigAgent  # type: ignore
    YAML_AVAILABLE = True
except Exception:
    YAML_AVAILABLE = False

class TestAgents(unittest.TestCase):
    def test_research_agent(self):
        agent = ResearchAgent()
        result = agent.run('ai marketing')
        self.assertIn('researched', result)

    def test_config_agent_load(self):
        if not YAML_AVAILABLE:
            self.skipTest('yaml library not available')
        agent = ConfigAgent()
        settings = agent.load_settings()
        self.assertIsInstance(settings, dict)
        result = agent.run('')
        self.assertTrue(result.startswith('ConfigAgent loaded'))

if __name__ == '__main__':
    unittest.main()
