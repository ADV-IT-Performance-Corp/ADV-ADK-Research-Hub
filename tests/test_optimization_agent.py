import unittest

from o3research.agents import OptimizationAgent


class TestOptimizationAgent(unittest.TestCase):
    def test_optimize_metric(self) -> None:
        agent = OptimizationAgent()
        result = agent.run("CTR")
        self.assertEqual(result, "OptimizationAgent optimizes for CTR")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
