import unittest

from optimization.prompt_tuner import PromptTuner


class TestPromptTuner(unittest.TestCase):
    def test_tune_combines_feedback(self) -> None:
        tuner = PromptTuner()
        result = tuner.tune("Promote webinar", ["add urgency", "mention speakers"])
        self.assertIn("refined", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
