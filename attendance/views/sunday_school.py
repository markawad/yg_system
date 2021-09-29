from django.shortcuts import render, redirect
from attendance.selectors.attendance import AttendanceSelector
from config.selectors.student import StudentSelector


def sunday_school(request):
    context = {
        'title': "Sunday School",
        'student_names': StudentSelector().get_all_student_names(),
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_sunday_school=True),
    }
    return render(request, 'attendance/sunday_school.html', context)
