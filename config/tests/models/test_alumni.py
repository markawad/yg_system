from config.tests.base import BaseTestCase


class AlumniTestCase(BaseTestCase):

    def test_printing_alumni_displays_full_name(self):
        self.assertEqual(str(self.alumni), 'Dani Smithy Smith')

