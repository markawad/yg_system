from config.tests.base import BaseTestCase
from bank.services.card import CardService
from django.core.exceptions import ValidationError


class CardTestCase(BaseTestCase):

    def test_card_str_function(self):
        card = CardService().create_card(holder=self.student, number=1234)
        self.assertEqual(str(card), "Mark Smithy Smith's balance: 0, type: Basic")

    def test_deposit_money_works(self):
        card = CardService().create_card(holder=self.student, number=1234)
        CardService().add_money(card=card, amount=50)
        self.assertEqual(card.balance, 50)

        CardService().add_money(card=card, amount=50)
        self.assertEqual(card.balance, 100)

    def test_validation_error_raised_when_depositing_more_than_max_deposit(self):
        card = CardService().create_card(holder=self.student, number=1234)
        _max = card.max_transaction
        with self.assertRaisesMessage(ValidationError, 'Amount exceeds maximum transaction limit.'):
            CardService().add_money(card=card, amount=_max + 1)

    def test_withdraw_money_works(self):
        card = CardService().create_card(holder=self.student, number=1234)
        CardService().add_money(card=card, amount=50)
        CardService().take_money(card=card, amount=20)

        self.assertEqual(card.balance, 30)

    def test_validation_error_raised_when_withdrawing_more_than_balance(self):
        card = CardService().create_card(holder=self.student, number=1234)
        CardService().add_money(card=card, amount=50)
        with self.assertRaisesMessage(ValidationError, 'Cannot withdraw more than actual balance'):
            CardService().take_money(card=card, amount=60)

    def test_validation_error_raised_when_withdrawing_more_than_max_limit(self):
        card = CardService().create_card(holder=self.student, number=1234)
        CardService().add_money(card=card, amount=100)
        CardService().add_money(card=card, amount=100)
        with self.assertRaisesMessage(ValidationError, 'Amount exceeds maximum transaction limit'):
            CardService().take_money(card=card, amount=150)

    def test_balance_rounds_decimals_correctly(self):
        card = CardService().create_card(holder=self.student, number=1234)
        CardService().add_money(card=card, amount=10.4)
        self.assertEqual(card.balance, 10)

        CardService().add_money(card=card, amount=10.6)
        self.assertEqual(card.balance, 21)

    def test_cannot_withdraw_in_decimals(self):
        card = CardService().create_card(holder=self.student, number=1234)
        CardService().add_money(card=card, amount=10)
        with self.assertRaisesMessage(ValidationError, 'Cannot withdraw in decimals'):
            CardService().withdraw_money(card=card, amount=9.7)

    def test_cannot_deposit_negative_values(self):
        card = CardService().create_card(holder=self.student, number=1234)
        with self.assertRaisesMessage(ValidationError, 'Negative values are not accepted.'):
            CardService().deposit_money(card, -20)

    def test_cannot_withdraw_negative_values(self):
        card = CardService().create_card(holder=self.student, number=1234)
        with self.assertRaisesMessage(ValidationError, 'Negative values are not accepted.'):
            CardService().withdraw_money(card, -20)
