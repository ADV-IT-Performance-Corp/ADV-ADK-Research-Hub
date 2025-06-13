import unittest

from agents.build_assistant import plan_and_apply


class TestBuildAssistant(unittest.TestCase):
    def test_plan_and_apply_returns_none(self) -> None:
        result = plan_and_apply("dummy plan")
        self.assertIsNone(result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
