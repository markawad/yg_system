from django.shortcuts import redirect, render


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('config:login')
    
    return render(request, 'home.html')
