from bank.models.transaction import Transaction


class TransactionSelector:

    @staticmethod
    def get_total_transaction_count():
        return Transaction.objects.count()

    @staticmethod
    def get_first_transaction_by_student(student):
        return Transaction.objects.filter(card=student.card)[0]

    @staticmethod
    def get_latest_transaction_by_student(student):
        return Transaction.objects.filter(card=student.card).order_by('-created_on')[0]

    @staticmethod
    def get_all_transactions_by_card(card_number):
        return Transaction.objects.select_related('card__holder')\
            .filter(card__number=card_number).order_by('-created_on')
