from config.tests.base import BaseTestCase
from config.services.bonus import BonusService
from config.selectors.bonus import BonusSelector


class BonusTestCase(BaseTestCase):

    def test_bonus_is_created(self):
        self.assertTrue(not BonusService().record_exists())
        BonusService().add_bonus_values(week=5, month=10, quarter=50)
        self.assertTrue(BonusService().record_exists())

    def test_bonus_is_updated(self):
        BonusService().add_bonus_values(week=5, month=10, quarter=50)
        BonusService().add_bonus_values(week=10, month=20, quarter=50)
        weekly_bonus = BonusSelector().get_weekly_bonus()
        self.assertEqual(weekly_bonus, 10)
