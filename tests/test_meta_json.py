import unittest
import json

class TestMetaEvaluationFile(unittest.TestCase):
    def test_required_sections_present(self):
        with open('docs/meta/meta_evaluation.json', 'r') as f:
            data = json.load(f)
        self.assertIn('evaluation_metrics', data)
        self.assertIn('evaluation_workflow', data)
        self.assertIn('version_history', data)

class TestPromptGenomeFile(unittest.TestCase):
    def test_active_version_present(self):
        with open('VERSION') as vf:
            version = vf.read().strip()
        with open('docs/meta/prompt_genome.json', 'r') as f:
            genome = json.load(f)
        prompts = genome.get('prompt_genome', {}).get('prompts', [])
        found = any(
            p.get('status') == 'active' and version in (p.get('id', '') + p.get('name', ''))
            for p in prompts
        )
        self.assertTrue(found, f'Active prompt for version {version} not found')

if __name__ == '__main__':
    unittest.main()
