from django.db.models import Sum
from bank.models import Card


class CardSelector:

    @staticmethod
    def get_card_by_number(card_number):
        return Card.objects.get(number=card_number)

    @staticmethod
    def get_student_by_card_number(card_number):
        card = Card.objects.select_related('holder').get(number=card_number)
        return card.holder

    @staticmethod
    def get_total_money_in_bank():
        return Card.objects.aggregate(Sum('balance'))['balance__sum']

    @staticmethod
    def get_all_cards():
        return Card.objects.select_related('holder').all()

