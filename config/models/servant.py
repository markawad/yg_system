from django.db import models
from phone_field import PhoneField


class Servant(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField()
    phone = PhoneField(help_text='Contact phone number')

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
