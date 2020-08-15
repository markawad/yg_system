from config.tests.base import BaseTestCase
from bank.services.card import CardService
from bank.services.transaction import TransactionService
from bank.selectors.transaction import TransactionSelector
from django.core.exceptions import ValidationError


class TransactionTestCase(BaseTestCase):

    def test_deposit_transaction_created(self):
        card = CardService().create_card(holder=self.student)
        CardService().deposit_money(card=card, amount=50)
        count = TransactionSelector().get_total_transaction_count()
        self.assertEqual(count, 1)
        transaction = TransactionSelector().get_first_transaction_by_student(student=self.student)
        self.assertIn(f'{str(transaction.card.holder)} added {transaction.amount} kudos to bank.',
                      str(transaction))

    def test_validation_error_raised_for_more_than_for(self):
        card = CardService().create_card(holder=self.student)
        with self.assertRaisesMessage(ValidationError, 'Transaction: Only one for needs to be true.'):
            TransactionService().create_transaction(card=card,
                                                    amount=50,
                                                    for_bank=True,
                                                    for_shop=True)
        with self.assertRaisesMessage(ValidationError, 'Transaction: Only one for needs to be true.'):
            TransactionService().create_transaction(card=card,
                                                    amount=50,
                                                    for_bank=True,
                                                    for_shop=True,
                                                    for_attendance=True)

    def test_withdrawing_transaction_is_negative(self):
        card = CardService().create_card(holder=self.student)
        CardService().deposit_money(card=card, amount=50)

        CardService().withdraw_money(card=card, amount=50)
        count = TransactionSelector().get_total_transaction_count()
        self.assertEqual(count, 2)

        transaction = TransactionSelector().get_latest_transaction_by_student(student=self.student)
        self.assertIn(f'{str(transaction.card.holder)} withdrew {transaction.amount} kudos from bank.',
                      str(transaction))
        self.assertTrue(transaction.is_negative)
