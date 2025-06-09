import unittest
import time
from o3research.agents.content_agent import ContentAgent
from o3research.agents.analytics_agent import AnalyticsAgent
from o3research.agents.ab_testing_agent import AbTestingAgent
from o3research.agents.governance_agent import GovernanceAgent


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

    def test_governance_agent_detects_stale_heartbeat(self):
        agent = GovernanceAgent()
        agent.record_heartbeat('AnalyticsAgent', time.time() - 31)
        result = agent.run('ok')
        self.assertIn('ALERT', result)
        self.assertIn('AnalyticsAgent', result)

    def test_governance_agent_no_alert_for_recent_heartbeat(self):
        agent = GovernanceAgent()
        agent.record_heartbeat('ContentAgent')
        result = agent.run('ok')
        self.assertNotIn('ALERT', result)


if __name__ == '__main__':
    unittest.main()
