from attendance.selectors.day import DaySelector
from datetime import datetime


def get_attendance_days_this_month():
    days = DaySelector().get_dates_by_month(month=datetime.today().month, for_sunday_school=True)
    print(days)


get_attendance_days_this_month()
