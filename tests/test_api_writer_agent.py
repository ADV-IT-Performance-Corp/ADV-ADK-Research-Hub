import unittest

from o3research.agents import ApiWriterAgent


class TestApiWriterAgent(unittest.TestCase):
    def test_send_message(self) -> None:
        agent = ApiWriterAgent()
        result = agent.run("hello")
        self.assertEqual(result, "ApiWriterAgent sent: hello")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
