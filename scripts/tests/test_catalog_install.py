import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


catalog = load('check_catalog', 'scripts/check_catalog.py')
copying = load('copy_skill', 'scripts/copy_skill.py')


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skill installation ')
        self.addCleanup(self.temp.cleanup)
        self.target = Path(self.temp.name) / 'host skills'
        self.target.mkdir()

    def install(self, *arguments):
        return subprocess.run(['bash', str(ROOT / 'scripts/install.sh'), '-T', str(self.target), *arguments], capture_output=True, text=True)

    def test_links_are_idempotent_and_uninstall_preserves_foreign_content(self):
        foreign = self.target / 'my-custom-skill'
        foreign.mkdir()
        (foreign / 'SKILL.md').write_text('user content')
        for _ in range(2):
            result = self.install('backend')
            self.assertEqual(result.returncode, 0, result.stderr)
        links = [entry for entry in self.target.iterdir() if entry.is_symlink()]
        self.assertEqual(len(links), 9)
        result = self.install('-u', 'backend')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.target.iterdir()), [foreign])
        self.assertEqual((foreign / 'SKILL.md').read_text(), 'user content')

    def test_retired_links_migrate_but_copies_and_foreign_links_survive(self):
        (self.target / 'tdd-workflow').symlink_to(ROOT / 'quality/tdd-workflow')
        (self.target / 'clean-code').mkdir()
        (self.target / 'clean-code/user.txt').write_text('keep')
        (self.target / 'systematic-debugging').symlink_to('/tmp/unrelated-debugging-skill')
        result = self.install('quality')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.target / 'tdd-workflow').is_symlink())
        self.assertEqual((self.target / 'clean-code/user.txt').read_text(), 'keep')
        self.assertEqual((self.target / 'systematic-debugging').readlink(), Path('/tmp/unrelated-debugging-skill'))

    def test_category_selection_does_not_remove_other_retired_links(self):
        (self.target / 'tdd-workflow').symlink_to(ROOT / 'quality/tdd-workflow')
        self.assertEqual(self.install('backend').returncode, 0)
        self.assertTrue((self.target / 'tdd-workflow').is_symlink())

    def test_copy_is_standalone_and_preserves_edits_without_force(self):
        result = self.install('-c', 'backend')
        self.assertEqual(result.returncode, 0, result.stderr)
        validator = self.target / 'api-patterns/scripts/api_validator.py'
        self.assertTrue(validator.is_file())
        self.assertFalse(validator.is_symlink())
        for readme in (self.target / 'api-patterns').glob('*.md'):
            self.assertTrue(readme.is_file())
        custom = self.target / 'api-patterns/SKILL.md'
        custom.write_text('user edit')
        self.assertEqual(self.install('-c', 'backend').returncode, 0)
        self.assertEqual(custom.read_text(), 'user edit')
        self.assertEqual(self.install('-c', '-f', 'backend').returncode, 0)
        self.assertNotEqual(custom.read_text(), 'user edit')
        self.assertFalse((self.target / 'oauth/examples/authorization-code/node_modules').exists())
        if importlib.util.find_spec('openapi_spec_validator'):
            sample = self.target / 'valid.json'
            sample.write_text('{"openapi":"3.1.0","info":{"title":"Fixture","version":"1"},"paths":{}}')
            process = subprocess.run([sys.executable, str(validator), str(sample)], capture_output=True, text=True)
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)

    def test_copy_does_not_clobber_broken_foreign_link_without_force(self):
        link = self.target / 'node'
        link.symlink_to('/tmp/no-such-foreign-node-skill')
        self.assertEqual(self.install('-c', 'backend').returncode, 0)
        self.assertEqual(link.readlink(), Path('/tmp/no-such-foreign-node-skill'))

    def test_invalid_category_is_rejected_before_installation(self):
        result = self.install('../backend')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_copy_excludes_caches_and_dereferences_resources(self):
        source = Path(self.temp.name) / 'source'
        source.mkdir()
        (source / 'SKILL.md').write_text('fixture')
        (source / 'node_modules').mkdir()
        (source / 'node_modules/generated').write_text('cache')
        (source / 'reference.md').write_text('reference')
        (source / 'linked.md').symlink_to('reference.md')
        copying.copy_skill(source, self.target / 'copy')
        self.assertEqual((self.target / 'copy/linked.md').read_text(), 'reference')
        self.assertFalse((self.target / 'copy/linked.md').is_symlink())
        self.assertFalse((self.target / 'copy/node_modules').exists())


class CatalogTests(unittest.TestCase):
    def test_current_catalog_is_valid_and_read_only(self):
        tracked = [ROOT / 'backend/api-patterns/scripts/api_validator.py', ROOT / 'skills/tdd']
        times = [path.lstat().st_mtime_ns for path in tracked]
        entries, problems = catalog.validate(ROOT, check_only=True)
        self.assertEqual(problems, [])
        self.assertEqual(len(entries), 67)
        self.assertEqual([path.lstat().st_mtime_ns for path in tracked], times)

    def test_links_detect_nested_resources_and_skip_fenced_examples(self):
        links = list(catalog.markdown_links('[real](references/deep/file.md#section)\n```md\n[fake](missing.md)\n```\n[spaced](<assets/my image.svg>)\n'))
        self.assertEqual(links, ['references/deep/file.md#section', 'assets/my image.svg'])

    def test_bundle_rebuild_preserves_unexpected_real_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for category in catalog.CATEGORIES:
                (root / category).mkdir()
                (root / category / 'README.md').write_text('# Fixture\n')
            for name in ('README.md', 'MIGRATION.md'):
                (root / name).write_text('# Fixture\n')
            (root / 'scripts').mkdir()
            (root / 'scripts/retired-skills.json').write_text('{}')
            for name in ('api-documentation-master', 'api-patterns'):
                (root / 'backend' / name / 'scripts').mkdir(parents=True)
            source = root / 'backend/api-documentation-master/scripts'
            (source / 'api_validator.py').write_text('#!/usr/bin/env python3\nprint("fixture")\n')
            (source / 'requirements.txt').write_text('fixture\n')
            (root / 'skills/user-data').mkdir(parents=True)
            (root / 'skills/user-data/keep.txt').write_text('important')
            _, problems = catalog.validate(root)
            self.assertTrue(any('real files are never removed' in problem for problem in problems))
            self.assertEqual((root / 'skills/user-data/keep.txt').read_text(), 'important')


if __name__ == '__main__':
    unittest.main()
