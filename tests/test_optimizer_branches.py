import unittest
from unittest.mock import MagicMock
from o3research.marketing import PerformanceOptimizer

class TestOptimizerBranches(unittest.TestCase):
    def test_suggest_adjustments_low_high(self):
        opt = PerformanceOptimizer(api_writer=MagicMock())
        low = opt.suggest_adjustments({'ROAS': 0.5, 'CTR': 0.01})
        high = opt.suggest_adjustments({'ROAS': 3.0, 'CTR': 0.03})
        mid = opt.suggest_adjustments({'ROAS': 1.5, 'CTR': 0.03})
        self.assertIn('decrease budget', low)
        self.assertIn('increase budget', high)
        self.assertIn('maintain budget', mid)
