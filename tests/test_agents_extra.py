import unittest
from src.agents.content_agent import ContentAgent
from src.agents.analytics_agent import AnalyticsAgent
from src.agents.ab_testing_agent import AbTestingAgent


class TestExtraAgents(unittest.TestCase):
    def test_content_agent(self):
        agent = ContentAgent()
        output = agent.run('LLM applications')
        self.assertIn('blog post', output)

    def test_analytics_agent(self):
        agent = AnalyticsAgent()
        output = agent.run('metrics data')
        self.assertIn('analyzed data', output)

    def test_ab_testing_agent_selects_best_variant(self):
        agent = AbTestingAgent()
        variants = {
            'A': {'clicks': 100, 'conversions': 5},
            'B': {'clicks': 120, 'conversions': 20},
            'C': {'clicks': 50, 'conversions': 5},
        }
        result = agent.run(variants)
        self.assertIn('B', result)


if __name__ == '__main__':
    unittest.main()
