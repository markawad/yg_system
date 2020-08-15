from django.db import models


class Bonus(models.Model):
    WEEK = models.PositiveSmallIntegerField()
    MONTH = models.PositiveSmallIntegerField()
    QUARTER = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'attendance bonus'

    def __str__(self):
        return f'WEEK: {self.WEEK}, MONTH: {self.MONTH}, QUARTER: {self.QUARTER}'
