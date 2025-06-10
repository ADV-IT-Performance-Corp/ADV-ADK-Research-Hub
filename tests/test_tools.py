import unittest

from o3research.core.tools import sanitize_input, format_table


class TestSanitizeInput(unittest.TestCase):
    def test_remove_control_chars(self):
        s = "ab\x00c\x07d\n"
        self.assertEqual(sanitize_input(s), "abcd\n")

    def test_recursive_structures(self):
        data = ["x\x01", {"a": "b\x02", "c": ["d\x03", "ok"]}]
        cleaned = sanitize_input(data)
        self.assertEqual(cleaned, ["x", {"a": "b", "c": ["d", "ok"]}])

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            sanitize_input(123)

    def test_invalid_nested_type(self):
        with self.assertRaises(ValueError):
            sanitize_input([object()])


class TestFormatTable(unittest.TestCase):
    def test_format_basic(self):
        rows = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
        table = format_table(rows, ["a", "b"])
        lines = table.splitlines()
        self.assertEqual(lines[0].strip(), "| a | b |")
        self.assertEqual(len(lines), 4)

    def test_auto_headers_and_long_values(self):
        rows = [{"col": "value" * 5}]
        table = format_table(rows, headers=None)
        self.assertIn("valuevaluevaluevaluevalue", table)

    def test_missing_headers_and_empty(self):
        self.assertEqual(format_table([], ["a"]), "")
        rows = [{"a": 1}]
        table = format_table(rows, ["a", "b"])
        self.assertTrue(table.endswith(" |"))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            format_table("bad", ["a"])
        with self.assertRaises(ValueError):
            format_table(123, ["a"])
        with self.assertRaises(ValueError):
            format_table([1], ["a"])
        with self.assertRaises(ValueError):
            format_table([{}], [1])


if __name__ == "__main__":
    unittest.main()
