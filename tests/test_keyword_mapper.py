import unittest

from o3research.research import KeywordMapperAgent


class TestKeywordMapperAgent(unittest.TestCase):
    def test_run_returns_top_keywords(self) -> None:
        csv_data = "keyword,volume\nai,100\ncloud,50\nedge,25\n"
        agent = KeywordMapperAgent()
        result = agent.run(csv_data)
        self.assertIn("ai", result)
        self.assertIn("cloud", result)
        self.assertTrue(result.startswith("Top keywords:"))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
