from bank.models.card import Card
from .transaction import TransactionService
from django.core.exceptions import ValidationError


class CardService:

    @staticmethod
    def create_card(holder):
        return Card.objects.create(holder=holder)

    @staticmethod
    def save(card):
        return card.save()

    def add_money(self, card, amount):
        self.validate_max_per_transaction(card=card, amount=amount)
        card.balance += round(amount)
        self.save(card)

    @staticmethod
    def validate_max_per_transaction(card, amount):
        if amount > card.max_transaction:
            raise ValidationError('Amount exceeds maximum transaction limit.')

    def take_money(self, card, amount):
        self.validate_max_per_transaction(card=card, amount=amount)
        self.validate_balance_greater_than_withdrawn(card=card, amount=amount)

        if int(amount) != amount:
            raise ValidationError('Cannot withdraw in decimals')
        card.balance -= amount
        self.save(card)

    @staticmethod
    def validate_balance_greater_than_withdrawn(card, amount):
        if card.balance < amount:
            raise ValidationError('Cannot withdraw more than actual balance')

    def deposit_money(self, card, amount):
        self.add_money(card=card, amount=amount)
        TransactionService().create_transaction(card=card, amount=amount, for_bank=True)

    def withdraw_money(self, card, amount):
        self.take_money(card=card, amount=amount)
        TransactionService().create_transaction(card=card, amount=amount, is_negative=True, for_bank=True)

    def add_attendance_bonus(self, card, amount):
        self.add_money(card=card, amount=amount)
        TransactionService().create_transaction(card=card, amount=amount, for_attendance=True)
