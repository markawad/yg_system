from django.shortcuts import render, redirect


def sunday_school(request):
    context = {
        'title': "Sunday School"
    }
    return render(request, 'attendance/sunday_school.html', context)
