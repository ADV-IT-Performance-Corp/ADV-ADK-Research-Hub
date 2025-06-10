import unittest
from tempfile import TemporaryDirectory

from o3research.core.task_flow import TaskFlow


class TestTaskFlow(unittest.TestCase):
    def test_process_order(self) -> None:
        with TemporaryDirectory() as tmpdir:
            flow = TaskFlow(queue_size=2, work_dir=tmpdir)
            results: list[str] = []

            def first() -> None:
                results.append("first")

            def second() -> None:
                results.append("second")

            flow.feed([first, second])
            flow.run()
            self.assertEqual(results, ["first", "second"])

    def test_empty_tasks_error(self) -> None:
        with TemporaryDirectory() as tmpdir:
            flow = TaskFlow(queue_size=1, work_dir=tmpdir)
            with self.assertRaises(ValueError):
                flow.feed([])

    def test_stop_clears_queue(self) -> None:
        with TemporaryDirectory() as tmpdir:
            flow = TaskFlow(queue_size=3, work_dir=tmpdir)

            def dummy() -> None:
                pass

            flow.feed([dummy, dummy])
            flow.stop()
            self.assertEqual(flow.pending(), 0)


if __name__ == "__main__":
    unittest.main()
