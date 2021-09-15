from django.shortcuts import render, redirect
from config.selectors.student import StudentSelector


def bible_study(request):
    context = {
        'title': "Bible Study",
        'student_names': StudentSelector().get_all_student_names()
    }
    return render(request, 'attendance/bible_study.html', context)
