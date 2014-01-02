from django.test import TransactionTestCase as TestCase


class testExportCourses(TestCase):
    fixtures = ['test-fixtures.json']

    def testXlsExport(self):
        from django.core import management
        import os
        with open('/tmp/command_output', 'w') as f:
            management.call_command('export-courses', xls_filename='/tmp/test-export.xls', stdout=f)

        with open('/tmp/command_output', 'r') as f:
            self.assertIn('Wrote 4 courses to /tmp/test-export.xls', f.read())

        os.remove('/tmp/command_output')