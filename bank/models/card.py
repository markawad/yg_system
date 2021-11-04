from django.db import models
from config.models.student import Student


class Card(models.Model):
    number = models.BigIntegerField(unique=True)
    holder = models.OneToOneField(
        Student,
        related_name='card',
        on_delete=models.CASCADE
    )

    class CardType(models.TextChoices):
        BASIC = 'Basic'
        GOLD = 'Gold'
        PLATINUM = 'Platinum'

    type = models.CharField(max_length=15, choices=CardType.choices, default=CardType.BASIC)
    balance = models.PositiveIntegerField(default=0)
    max_transaction = models.PositiveIntegerField(default=500)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('config:bank:user_profile', args=[str(self.number)])

    def __str__(self):
        return f'{str(self.holder)}\'s balance: {self.balance}, type: {self.type}'

