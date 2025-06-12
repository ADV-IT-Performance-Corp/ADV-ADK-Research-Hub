import unittest

from o3research.web.landing_page_creator import create_landing_page


class TestLandingPageCreator(unittest.TestCase):
    def test_default_template(self) -> None:
        html = create_landing_page("product", "value")
        self.assertIn("<h1>", html)
        self.assertIn("product", html)
        self.assertIn("value", html)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
