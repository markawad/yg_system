from attendance.tests.base import BaseTestCase
from attendance.selectors.day import DaySelector
from datetime import datetime


class DayTestCase(BaseTestCase):

    def test_get_dates_of_this_month(self):
        days = DaySelector.get_dates_by_month(datetime.now().month, for_sunday_school=True)
        self.assertEqual(len(days), 1)
