from django.shortcuts import render, redirect
from attendance.selectors.attendance import AttendanceSelector
from config.selectors.student import StudentSelector


def bible_study(request):
    context = {
        'title': "Bible Study",
        'student_names': StudentSelector().get_all_student_names(),
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_bible_study=True),
    }
    return render(request, 'attendance/bible_study.html', context)
