from django.urls import path, include
from . import views

app_name = 'bank'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('user/', views.scan_card, name='scan_card'),
    path('user/<int:card_number>/', views.user_profile, name='user_profile'),
    path('user/<int:card_number>/deposit', views.deposit_money, name='deposit'),
    path('user/<int:card_number>/withdraw', views.withdraw_money, name='withdraw'),
    path('total_money/', views.total_money, name='total_money'),
]
