import unittest

from o3research.marketing import PerformanceOptimizer
from o3research.agents import ApiWriterAgent


class DummyWriter(ApiWriterAgent):
    def __init__(self) -> None:
        super().__init__()
        self.last_message = None

    def run(self, message: str) -> str:  # type: ignore[override]
        self.last_message = message
        return f"SENT: {message}"


class TestPerformanceOptimizer(unittest.TestCase):
    def test_analyze_and_forward(self) -> None:
        writer = DummyWriter()
        optimizer = PerformanceOptimizer(api_writer=writer)
        metrics = [
            {
                "impressions": 1000,
                "clicks": 10,
                "cost": 50.0,
                "conversions": 1,
                "revenue": 20.0,
            }
        ]
        result = optimizer.analyze_and_forward(metrics)
        self.assertIn("SENT", result)
        self.assertIsNotNone(writer.last_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
