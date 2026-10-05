"""Regression guards for the checkout outage and production publishing boundary."""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    # BaseLoader preserves Actions' `on` key instead of treating it as a boolean.
    return yaml.load((ROOT / '.github/workflows' / name).read_text(), Loader=yaml.BaseLoader)


class ReleaseWorkflowTests(unittest.TestCase):
    def test_publishing_needs_no_personal_token_or_repository_write(self):
        deploy = workflow('deploy.yml')
        self.assertEqual(deploy['permissions'], {'contents': 'read'})
        self.assertNotIn('permissions', deploy['jobs']['build'])
        self.assertEqual(deploy['jobs']['deploy']['permissions'], {
            'pages': 'write', 'id-token': 'write',
        })
        text = (ROOT / '.github/workflows/deploy.yml').read_text()
        self.assertNotIn('secrets.', text)
        for command in ('git push', 'git reset', 'git commit'):
            self.assertNotIn(command, text)
        checkout = deploy['jobs']['build']['steps'][0]
        self.assertEqual(checkout['with'], {'persist-credentials': 'false'})

    def test_prs_and_manual_non_main_runs_cannot_publish(self):
        deploy = workflow('deploy.yml')
        self.assertIn('pull_request', deploy['on'])
        self.assertIn('workflow_dispatch', deploy['on'])
        self.assertEqual(deploy['jobs']['deploy']['needs'], 'build')
        self.assertEqual(deploy['jobs']['deploy']['if'],
                         "github.ref == 'refs/heads/main' && github.event_name != 'pull_request'")
        self.assertEqual(deploy['concurrency']['cancel-in-progress'], 'false')
        self.assertIn('github.event.pull_request.number', deploy['concurrency']['group'])

    def test_only_the_built_and_browser_tested_artifact_is_uploaded(self):
        steps = workflow('deploy.yml')['jobs']['build']['steps']
        build = next(i for i, s in enumerate(steps) if 'npm run build' in s.get('run', ''))
        test = next(i for i, s in enumerate(steps) if s.get('run') == 'npm test')
        upload = next(i for i, s in enumerate(steps) if s.get('uses', '').startswith('actions/upload-pages-artifact@'))
        self.assertLess(build, test)
        self.assertLess(test, upload)
        self.assertEqual(steps[upload]['with']['path'], 'website/dist')
        for step in steps[build:upload + 1]:
            self.assertNotIn('continue-on-error', step)
            self.assertNotIn('if', step)
        self.assertTrue(any('source-revision.txt' in s.get('run', '') for s in steps[test:upload]))

    def test_one_main_only_writer_preserves_all_generated_products(self):
        writer = workflow('generated-data.yml')
        job = writer['jobs']['generate']
        self.assertEqual(job['if'], "github.ref == 'refs/heads/main'")
        self.assertNotIn('pull_request', writer['on'])
        self.assertEqual(writer['concurrency'], {'group': 'generated-data', 'cancel-in-progress': 'false'})
        self.assertEqual(job['steps'][0]['with']['ref'], 'main')
        run = '\n'.join(s.get('run', '') for s in job['steps'])
        for command in ('python bin/sigma-gen.py --skip-yaml-update',
                        'python bin/site.py', 'python bin/update_badge.py',
                        'git diff --exit-code -- yaml/'):
            self.assertIn(command, run)
        pr = job['steps'][-1]['with']
        self.assertEqual(pr['base'], 'main')
        self.assertEqual(pr['branch'], 'automation/generated-data')
        self.assertEqual(set(pr['add-paths'].splitlines()), {
            'detections/', 'website/public/api/',
            'website/public/rmm_tools_table.csv', 'rmm-tools-count.json',
        })
        for path in ('website/public/**', 'detections/**', 'rmm-tools-count.json'):
            self.assertNotIn(path, writer['on']['push']['paths'])
        for old_writer in ('sigma-gen.yml', 'update-badge.yml'):
            self.assertFalse((ROOT / '.github/workflows' / old_writer).exists())
        for path in (ROOT / '.github/workflows').glob('*.yml'):
            self.assertNotIn('PUSH_TOKEN', path.read_text(), str(path))


if __name__ == '__main__':
    unittest.main()
