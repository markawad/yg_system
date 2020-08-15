from django.db import models
from config.models.student import Student


class Multiplier(models.Model):
    student = models.OneToOneField(Student,
                                   related_name='multiplier',
                                   on_delete=models.CASCADE)
    sunday_school = models.IntegerField(default=0)
    bible_study = models.IntegerField(default=0)
    summer_club = models.IntegerField(default=0)
