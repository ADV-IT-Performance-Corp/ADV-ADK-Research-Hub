import unittest

from o3research.marketing import Budgeter
from o3research.agents.agent_registry import get_agent


class TestBudgeter(unittest.TestCase):
    def test_allocate(self) -> None:
        plans = {
            "search": {
                "plan": "Search campaign",
                "metrics": {
                    "impressions": 1000,
                    "clicks": 100,
                    "cost": 100.0,
                    "conversions": 10,
                    "revenue": 200.0,
                },
            },
            "social": {
                "plan": "Social campaign",
                "metrics": {
                    "impressions": 500,
                    "clicks": 50,
                    "cost": 50.0,
                    "conversions": 5,
                    "revenue": 80.0,
                },
            },
        }
        b = Budgeter()
        result = b.allocate(plans)
        self.assertAlmostEqual(result["search"], 66.67, places=2)
        self.assertAlmostEqual(result["social"], 33.33, places=2)

    def test_registry_lookup(self) -> None:
        cls = get_agent("budgeter")
        self.assertIs(cls, Budgeter)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
