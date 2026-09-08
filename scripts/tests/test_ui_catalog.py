import json
import shutil
import csv
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'frontend/ui-ux-pro-max/scripts/search.py'


class UICatalogTests(unittest.TestCase):
    def test_search_retains_catalogue_results(self):
        result = subprocess.run([sys.executable, str(SCRIPT), 'keyboard accessibility', '--domain', 'ux', '--json'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['results'])

    def test_persistence_paths_and_generated_references_match(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run([sys.executable, str(SCRIPT), 'analytics dashboard', '--design-system', '--persist', '-p', '../Example Product', '--page', '../Dashboard', '--output-dir', temp], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            folder = Path(temp) / 'design-system/example-product'
            master, page = folder / 'MASTER.md', folder / 'pages/dashboard.md'
            self.assertTrue(master.exists())
            self.assertTrue(page.exists())
            self.assertIn(str(master), result.stdout)
            self.assertIn(str(page), result.stdout)
            self.assertIn('`pages/[page-name].md`', master.read_text())
            self.assertIn('`../MASTER.md`', page.read_text())
            self.assertFalse((Path(temp) / 'Example Product').exists())

    def test_missing_catalogue_fails_search_and_generation_without_persisting(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copytree(SCRIPT.parent, root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
            for options in [['--domain', 'ux', '--json'], ['--design-system', '--persist']]:
                result = subprocess.run([sys.executable, str(root / 'scripts/search.py'), 'analytics', *options], cwd=root, capture_output=True, text=True)
                self.assertEqual(result.returncode, 2)
                self.assertFalse((root / 'design-system').exists())

    def test_all_bundled_data_matches_search_columns_and_contains_rows(self):
        spec = importlib.util.spec_from_file_location('ui_core_fixture', SCRIPT.parent / 'core.py')
        core = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(core)
        configs = list(core.CSV_CONFIG.values()) + [{**core._STACK_COLS, **config} for config in core.STACK_CONFIG.values()]
        for config in configs:
            with self.subTest(file=config['file']):
                with (SCRIPT.parent.parent / 'data' / config['file']).open() as stream:
                    reader = csv.DictReader(stream)
                    self.assertTrue(set(config['search_cols'] + config['output_cols']).issubset(reader.fieldnames))
                    self.assertTrue(list(reader))


if __name__ == '__main__':
    unittest.main()
