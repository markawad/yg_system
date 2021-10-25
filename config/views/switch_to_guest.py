from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from config.services.user import UserService


def switch_to_guest(request):

    if not request.user.is_authenticated:
        return redirect('config:login')

    logout(request)
    user = UserService.get_guest()
    login(request, user)
    
    return render(request, 'bank/home.html')
