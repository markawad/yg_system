from django.db import models
from config.models.student import Student
from .day import Day


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='attendance')
    by_card = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'day')

    def __str__(self):
        return f'{self.day.get_service()} - {self.day.date}: {self.student}'
