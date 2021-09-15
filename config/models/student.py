from django.core.exceptions import ValidationError
from django.db import models
from .servant import Servant
from phone_field import PhoneField


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField()
    grade = models.PositiveSmallIntegerField(
        choices=(
            (9, 'Grade 9'),
            (10, 'Grade 10'),
            (11, 'Grade 11'),
            (12, 'Grade 12'),
            (13, 'Grade 13'))
    )
    school = models.CharField(max_length=50)
    phone = PhoneField(help_text='Contact phone number')
    mothers_number = PhoneField(help_text='Mother\'s contact phone number', blank=True, null=True)
    fathers_number = PhoneField(help_text='Father\'s contact phone number', blank=True, null=True)
    father_of_confession = models.CharField(max_length=50, blank=True, null=True)
    servant = models.ForeignKey(
        Servant,
        related_name='students',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    residency_area = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
