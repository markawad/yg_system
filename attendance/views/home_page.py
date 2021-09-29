from django.shortcuts import render, redirect
from django.http import HttpResponse


def home_page(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

    return render(request, 'attendance/home.html')
