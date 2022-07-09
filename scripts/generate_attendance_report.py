import os
import sys
import csv
from datetime import date
from pathlib import Path
from config.selectors.student import StudentSelector
from attendance.selectors.day import DaySelector

if 'MONTH' not in os.environ:
    sys.exit('Failed to find env \'MONTH\'')

MONTH = os.environ.get('MONTH')
days = DaySelector().get_dates_by_month(month=MONTH, for_sunday_school=True)
all_students = StudentSelector().get_all_students()

with open(f'{Path.home()}/attendance_reports/{date.today().strftime("%B").lower()}-attendance_report.csv', 'w',
          encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow([''] + list(days))

    for student in all_students:
        line = [str(student)]
        for day in days:
            attendees = day.attendees.all()
            if student in attendees:
                line.append('present')
            else:
                line.append('')
        writer.writerow(line)
