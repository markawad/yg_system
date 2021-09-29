from django.shortcuts import render, redirect


def home_page(request):

    if not request.user.is_authenticated:
        return redirect('config:login')

    return render(request, 'attendance/home.html')
