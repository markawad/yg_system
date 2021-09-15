from django.shortcuts import render, redirect
from config.selectors.student import StudentSelector


def sunday_school(request):
    context = {
        'title': "Sunday School",
        'student_names': StudentSelector().get_all_student_names()
    }
    return render(request, 'attendance/sunday_school.html', context)
