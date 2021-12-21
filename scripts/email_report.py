import sys
from attendance.selectors.day import DaySelector, Day
from attendance.selectors.attendance import AttendanceSelector
from attendance.services import MultiplierService
from config.selectors.student import StudentSelector

yesterday: Day = DaySelector.get_yesterday_or_none()
if not yesterday:
    sys.exit(1)

all_students = StudentSelector.get_all_student_count()
unattended_students = AttendanceSelector.get_unattended_students_by_day(yesterday)
attended_students = all_students - unattended_students

report = f'''{yesterday.date} - {yesterday.get_service()}: Attendance Report

Unattended students : {len(unattended_students)}
Total students      : {len(all_students)}
% Attendance        : {(attended_students/all_students) * 100}%   

'''


def get_multiplier(student, day):
    multiplier = MultiplierService.get_or_create_multiplier(student)
    if day.for_sunday_school:
        return multiplier.sunday_school
    elif day.for_bible_study:
        return multiplier.bible_study
    return multiplier.summer_club


for student in unattended_students:
    multiplier = get_multiplier(student, yesterday)

    report += f'Unattended {abs(multiplier)} times - {student}'

print(report)
