from django.shortcuts import render, redirect


def summer_club(request):
    context = {
        'title': "Summer Club"
    }
    return render(request, 'attendance/summer_club.html', context)
