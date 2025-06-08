import unittest
from src.core.evaluation import evaluate

class TestEvaluation(unittest.TestCase):
    def test_weighted_score_full(self):
        metrics = {
            "clarity": 5,
            "completeness": 3,
            "alignment": 4,
            "efficiency": 2,
        }
        score = evaluate(metrics)
        self.assertAlmostEqual(score, 3.5)

    def test_weighted_score_partial(self):
        metrics = {
            "clarity": 4,
            "efficiency": 4,
        }
        score = evaluate(metrics)
        # Only clarity and efficiency weights (0.25 each) should be considered
        self.assertAlmostEqual(score, 4.0)

    def test_no_matching_weights(self):
        """Metrics with no matching weights should result in a score of 0."""
        metrics = {
            "nonexistent": 5,
            "another": 3,
        }
        score = evaluate(metrics)
        self.assertEqual(score, 0.0)

if __name__ == "__main__":
    unittest.main()
