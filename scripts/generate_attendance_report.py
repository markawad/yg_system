import os
import sys
import csv
import calendar
from datetime import date
from config.selectors.student import StudentSelector
from attendance.selectors.day import DaySelector

if 'MONTH' not in os.environ:
    sys.exit('Failed to find env \'MONTH\'')

MONTH = os.environ.get('MONTH')
days = DaySelector().get_dates_by_month(month=MONTH, for_sunday_school=True)
all_students = StudentSelector().get_all_students()

prefix = f'{date.today().year}-{calendar.month_name[int(MONTH)].lower()}'
path = f'{os.environ.get("PATH_report", "")}/{prefix}-attendance_report.csv'
with open(path, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['', ''] + list(days))

    for student in all_students:
        line = [str(student), student.phone]
        for day in days:
            attendees = day.attendees.all()
            if student in attendees:
                line.append('')
            else:
                line.append('absent')
        writer.writerow(line)
