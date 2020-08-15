from attendance.models.day import Day
from django.utils import timezone


class DayService:

    @staticmethod
    def add_attendance_day(for_sunday_school=False, for_bible_study=False):
        return Day.objects.get_or_create(date=timezone.localdate().today(),
                                         for_sunday_school=for_sunday_school,
                                         for_bible_study=for_bible_study)[0]
