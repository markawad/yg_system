from django.urls import path, include
from . import views

app_name = 'config'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bank/', include('bank.urls', namespace='bank')),
    path('attendance/', include('attendance.urls', namespace='attendance')),
]