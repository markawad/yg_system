from config.tests.base import BaseTestCase
from config.models.servant import Servant


class ServantTestCase(BaseTestCase):

    def test_printing_servant_displays_full_name(self):
        self.assertEqual(str(self.servant), 'John Smithy Smith')
