from django.db import IntegrityError
from config.tests.base import BaseTestCase
from bank.services.card import CardService


class CardTestCase(BaseTestCase):

    def test_cannot_add_card_number_that_already_exists(self):
        CardService().create_card(holder=self.student, number=1234)
        with self.assertRaises(IntegrityError):
            CardService().create_card(holder=self.student2, number=1234)

    def test_cannot_add_multiple_cards_for_one_student(self):
        CardService().create_card(holder=self.student, number=1234)
        with self.assertRaises(IntegrityError):
            CardService().create_card(holder=self.student, number=12345)
