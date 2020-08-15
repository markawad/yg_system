from django.db import models


class Discount(models.Model):
    BASIC = models.PositiveSmallIntegerField()
    GOLD = models.PositiveSmallIntegerField()
    PLATINUM = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'discount'
