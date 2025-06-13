import tempfile
import unittest
from o3research.web.landing_page_creator import create_landing_page, _load


class TestLandingPageCreatorExtra(unittest.TestCase):
    def test_load_helper_reads_file(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            f.write("content")
            name = f.name
        self.assertEqual(_load(name), "content")

    def test_custom_templates(self):
        with tempfile.NamedTemporaryFile("w", delete=False) as pt:
            pt.write("Headline: Hello\nSubheadline: World\n- bullet")
            pt_path = pt.name
        with tempfile.NamedTemporaryFile("w", delete=False) as ht:
            ht.write("<html>{bullets}-{cta}</html>")
            ht_path = ht.name
        html = create_landing_page(
            "Prod", "Value", prompt_template=pt_path, html_template=ht_path, cta="Go"
        )
        self.assertIn("bullet", html)
        self.assertIn("Go", html)
