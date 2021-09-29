from django.shortcuts import render, redirect
from attendance.selectors.attendance import AttendanceSelector
from config.selectors.student import StudentSelector


def summer_club(request):
    context = {
        'title': "Summer Club",
        'student_names': StudentSelector().get_all_student_names(),
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(),
    }
    return render(request, 'attendance/summer_club.html', context)
