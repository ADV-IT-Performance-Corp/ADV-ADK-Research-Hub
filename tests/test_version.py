import unittest
import src

class TestVersion(unittest.TestCase):
    def test_version_matches_file(self):
        with open('VERSION', 'r', encoding='utf-8') as f:
            self.assertEqual(src.__version__, f.read().strip())

if __name__ == '__main__':
    unittest.main()
