import unittest
from src.agents.content_agent import ContentAgent
from src.agents.analytics_agent import AnalyticsAgent


class TestExtraAgents(unittest.TestCase):
    def test_content_agent(self):
        agent = ContentAgent()
        output = agent.run('LLM applications')
        self.assertIn('blog post', output)

    def test_analytics_agent(self):
        agent = AnalyticsAgent()
        output = agent.run('metrics data')
        self.assertIn('analyzed data', output)


if __name__ == '__main__':
    unittest.main()
