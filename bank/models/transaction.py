from django.db import models
from .card import Card


class Transaction(models.Model):
    card = models.ForeignKey(
        Card,
        related_name='transactions',
        on_delete=models.CASCADE
    )
    for_bank = models.BooleanField(default=False)
    for_shop = models.BooleanField(default=False)
    for_attendance = models.BooleanField(default=False)
    is_negative = models.BooleanField(default=False)
    amount = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.for_bank:
            if not self.is_negative:
                return f'{self.created_on}: {str(self.card.holder)} added {self.amount} kudos to bank.'
            return f'{self.created_on}: {str(self.card.holder)} withdrew {self.amount} kudos from bank.'
        elif self.for_shop:
            return f'{self.created_on}: {str(self.card.holder)} paid {self.amount} kudos in shop.'
        return f'{self.created_on}: {str(self.card.holder)} received {self.amount} kudos for attendance.'
