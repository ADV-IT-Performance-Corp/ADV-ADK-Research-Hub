import unittest

from o3research.marketing import BudgetAllocatorAgent
from o3research.agents.agent_registry import get_agent


class TestBudgetAllocatorAgent(unittest.TestCase):
    def test_allocation_cpa(self) -> None:
        metrics = {
            "search": {"conversions": 30, "revenue": 1200},
            "social": {"conversions": 20, "revenue": 800},
        }
        agent = BudgetAllocatorAgent()
        result = agent.run(metrics, target=10, goal="CPA")
        self.assertIn("search: $300", result)
        self.assertIn("social: $200", result)
        self.assertIn("Daily budget: $16.67", result)

    def test_allocation_roas(self) -> None:
        metrics = {
            "search": {"conversions": 30, "revenue": 1200},
            "social": {"conversions": 20, "revenue": 800},
        }
        agent = BudgetAllocatorAgent()
        result = agent.run(metrics, target=2, goal="ROAS")
        self.assertIn("search: $600", result)
        self.assertIn("social: $400", result)
        self.assertIn("Daily budget: $33.33", result)

    def test_registry_lookup(self) -> None:
        cls = get_agent("budget_allocator")
        self.assertIs(cls, BudgetAllocatorAgent)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
