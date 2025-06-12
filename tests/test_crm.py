import json
import unittest
from unittest.mock import MagicMock, patch

from o3research.crm import sync_to_crm, LeadScoringAgent

class TestSyncToCrm(unittest.TestCase):
    @patch('o3research.crm.crm_sync.request.urlopen')
    def test_sync_success(self, mock_urlopen):
        resp = MagicMock()
        resp.read.return_value = json.dumps({'id': '123'}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = resp
        message = sync_to_crm({'name': 'n'}, 'tok', base_url='http://x')
        self.assertIn('123', message)
        mock_urlopen.assert_called_once()

class TestLeadScoringAgent(unittest.TestCase):
    def test_run_scores(self):
        agent = LeadScoringAgent()
        msg = agent.run({'name': 'Acme', 'industry': 'technology', 'annual_revenue': 2_000_000})
        self.assertIn('Acme', msg)
        self.assertIn('100', msg)
