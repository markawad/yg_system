from django.core.exceptions import ObjectDoesNotExist
from attendance.models.attendance import Attendance
from attendance.selectors.day import DaySelector
from config.selectors.student import StudentSelector
from datetime import datetime


class AttendanceSelector:

    @staticmethod
    def get_attendance_count_by_day(for_sunday_school=False, for_bible_study=False):
        try:
            return Attendance.objects.filter(day=DaySelector.get_date(for_sunday_school=for_sunday_school,
                                                                      for_bible_study=for_bible_study)).count()
        except ObjectDoesNotExist:
            return 0

    @staticmethod
    def get_unattended_students_by_day(day: datetime.date) -> set:
        attendence_objs = Attendance.objects.filter(day=day).select_related('student')
        attended_students = {attendance.student for attendance in attendence_objs}

        return StudentSelector.get_all_students() - attended_students
