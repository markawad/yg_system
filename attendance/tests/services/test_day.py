from attendance.tests.base import BaseTestCase
from attendance.services.day import DayService
from attendance.selectors.day import DaySelector
from attendance.models.day import Day
from django.db import IntegrityError
from django.utils import timezone


class DayTestCase(BaseTestCase):

    def test_no_duplicate_attendance_dates_in_db(self):
        DayService().add_attendance_day(for_sunday_school=True)
        DayService().add_attendance_day(for_sunday_school=True)
        self.assertEqual(Day.objects.filter(date=timezone.localdate().today(), for_sunday_school=True).count(), 1)

