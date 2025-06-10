import unittest

from o3research.core.context import Context


class TestContext(unittest.TestCase):
    def test_update_overwrites(self) -> None:
        ctx = Context({"a": 1, "b": 2})
        ctx.update({"b": 3, "c": 4})
        self.assertEqual(ctx["a"], 1)
        self.assertEqual(ctx["b"], 3)
        self.assertEqual(ctx["c"], 4)

    def test_update_invalid_type(self) -> None:
        ctx = Context()
        with self.assertRaises(TypeError):
            ctx.update([("a", 1)])

    def test_contains_getitem_to_dict(self) -> None:
        ctx = Context({"x": 42})
        self.assertTrue("x" in ctx)
        self.assertFalse("y" in ctx)
        self.assertEqual(ctx["x"], 42)
        self.assertEqual(ctx.to_dict(), {"x": 42})

    def test_init_invalid_type(self) -> None:
        with self.assertRaises(TypeError):
            Context([("a", 1)])


if __name__ == "__main__":
    unittest.main()
