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

    def test_initial_bonus_gets_added_if_no_record_exists(self):
        BonusService().add_bonus_values_if_not_exists(week=5, month=10, quarter=50)
        weekly_bonus = BonusSelector().get_weekly_bonus()
        self.assertEqual(weekly_bonus, 5)

    def test_initial_values_do_not_change_existing_ones(self):
        BonusService().add_bonus_values(week=5, month=10, quarter=50)
        BonusService().add_bonus_values_if_not_exists(week=10, month=25, quarter=50)
        bonus = BonusSelector().get_bonus_values()
        self.assertTrue(bonus.WEEK == 5 and bonus.MONTH == 10 and bonus.QUARTER == 50)
