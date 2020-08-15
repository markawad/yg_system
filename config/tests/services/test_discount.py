from config.tests.base import BaseTestCase
from config.services.discount import DiscountService
from config.selectors.discount import DiscountSelector


class BonusTestCase(BaseTestCase):

    def test_bonus_is_created(self):
        self.assertTrue(not DiscountService().record_exists())
        DiscountService().add_discount_values(basic=5, gold=10, platinum=50)
        self.assertTrue(DiscountService().record_exists())

    def test_bonus_is_updated(self):
        DiscountService().add_discount_values(basic=5, gold=10, platinum=50)
        DiscountService().add_discount_values(basic=5, gold=20, platinum=50)
        gold_discount = DiscountSelector().get_gold_discount()
        self.assertEqual(gold_discount, 20)
