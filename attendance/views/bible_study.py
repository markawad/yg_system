from django.shortcuts import render, redirect


def bible_study(request):
    context = {
        'title': "Bible Study"
    }
    return render(request, 'attendance/bible_study.html', context)
