from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'config'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bank/', include('bank.urls', namespace='bank')),
    path('attendance/', include('attendance.urls', namespace='attendance')),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='home.html'), name='logout'),
    path('switch/guest', views.switch_to_guest, name='switch_to_guest'),
]