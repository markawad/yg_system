from bank.models.transaction import Transaction
from django.core.exceptions import ValidationError


class TransactionService:

    def create_transaction(self, card, amount, is_negative=False,
                           for_bank=False, for_shop=False, for_attendance=False):
        self.validate_only_one_for_is_true(for_bank=for_bank, for_shop=for_shop, for_attendance=for_attendance)
        return Transaction.objects.create(card=card,
                                          amount=amount,
                                          is_negative=is_negative,
                                          for_bank=for_bank,
                                          for_shop=for_shop,
                                          for_attendance=for_attendance)

    @staticmethod
    def validate_only_one_for_is_true(for_bank, for_shop, for_attendance):
        if not (for_bank ^ for_shop ^ for_attendance) or (for_bank and for_shop and for_attendance):
            raise ValidationError('Transaction: Only one for needs to be true.')
