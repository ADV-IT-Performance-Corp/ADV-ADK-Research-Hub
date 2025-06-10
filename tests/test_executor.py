import asyncio
import unittest
from unittest.mock import patch

from o3research.core.executor import Executor


async def sample_task() -> str:
    return "done"


class TestExecutor(unittest.TestCase):
    def test_run_tasks_failure(self) -> None:
        executor = Executor()
        with patch(__name__ + ".sample_task", side_effect=RuntimeError("boom")):
            with self.assertLogs(executor.logger, level="ERROR") as cm:
                results = asyncio.run(executor.run_tasks([sample_task]))
        self.assertEqual(len(results), 1)
        result = results[0]
        self.assertFalse(result.success)
        self.assertEqual(result.error, "boom")
        self.assertIn("boom", cm.output[0])

    def test_run_tasks_success(self) -> None:
        executor = Executor()

        def good_sync() -> str:
            return "ok"

        results = asyncio.run(executor.run_tasks([good_sync]))
        self.assertEqual(len(results), 1)
        result = results[0]
        self.assertTrue(result.success)
        self.assertEqual(result.result, "ok")


if __name__ == "__main__":
    unittest.main()
