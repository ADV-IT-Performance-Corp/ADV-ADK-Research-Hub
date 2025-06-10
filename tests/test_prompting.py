import unittest

from o3research.core.prompt_manager import PromptManager


class TestPromptManager(unittest.TestCase):
    def test_summarize_long_history(self):
        mgr = PromptManager(history_limit=5)
        history = [f"msg {i}" for i in range(10)]
        result = mgr.summarize_history(history)
        # Should reduce number of messages and include summary token
        self.assertLess(len(result), len(history))
        self.assertTrue(result[0].startswith("["))

    def test_skip_summarization_for_short_history(self):
        mgr = PromptManager(history_limit=5)
        history = ["hello", "world"]
        result = mgr.summarize_history(history)
        self.assertEqual(result, history)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
