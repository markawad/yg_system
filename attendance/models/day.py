from django.db import models
from config.models.student import Student


class Day(models.Model):
    date = models.DateField()
    for_sunday_school = models.BooleanField(default=True)
    for_bible_study = models.BooleanField(default=False)
    attendees = models.ManyToManyField(Student, through='Attendance')

    class Meta:
        unique_together = ('date', 'for_sunday_school', 'for_bible_study')

    def get_service(self) -> str:
        if self.for_sunday_school:
            return 'Sunday School'
        elif self.for_bible_study:
            return 'Bible Study'
        return 'Summer Club'

    def __str__(self):
        return str(self.date)
