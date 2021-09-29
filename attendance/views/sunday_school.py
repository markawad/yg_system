from django.shortcuts import render, redirect
from attendance.selectors.attendance import AttendanceSelector
from config.selectors.student import StudentSelector
from django.http import HttpResponse


def sunday_school(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

    context = {
        'title': "Sunday School",
        'student_names': StudentSelector().get_all_student_names(),
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_sunday_school=True),
    }
    return render(request, 'attendance/sunday_school.html', context)
