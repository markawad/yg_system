from django.core.exceptions import ObjectDoesNotExist
from attendance.models.attendance import Attendance
from attendance.selectors.day import DaySelector


class AttendanceSelector:

    @staticmethod
    def get_attendance_count_by_day(for_sunday_school=False, for_bible_study=False):
        try:
            return Attendance.objects.filter(day=DaySelector.get_date(for_sunday_school=for_sunday_school,
                                                                      for_bible_study=for_bible_study)).count()
        except ObjectDoesNotExist:
            return 0
