from django.shortcuts import render, redirect
from config.selectors.student import StudentSelector


def summer_club(request):
    context = {
        'title': "Summer Club",
        'student_names': StudentSelector().get_all_student_names()
    }
    return render(request, 'attendance/summer_club.html', context)
