from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def switch_to_guest(request):

    if not request.user.is_authenticated:
        return redirect('config:login')

    logout(request)
    user = authenticate(username='guest', password='iamnotanadmin')
    login(request, user)
    
    return render(request, 'bank/home.html')
