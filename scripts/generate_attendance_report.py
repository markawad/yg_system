from attendance.selectors.day import DaySelector
from datetime import date


def get_attendance_days_this_month():
    days = DaySelector().get_dates_by_month(month=date.month, for_sunday_school=True)
    print(days)
