import unittest
from o3research.core.context import Context


class TestContextGet(unittest.TestCase):
    def test_get_with_default(self):
        ctx = Context({"a": 1})
        self.assertEqual(ctx.get("a"), 1)
        self.assertEqual(ctx.get("missing", 5), 5)
