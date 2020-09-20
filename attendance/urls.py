from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sunday_school/', views.sunday_school, name='sunday_school'),
    path('bible_study/', views.bible_study, name='bible_study'),
    path('summer_club/', views.summer_club, name='summer_club'),
    path('sunday_school/card', views.card_attendance_sunday_school, name='ss_attendance'),
    path('bible_study/card', views.card_attendance_bible_study, name='bs_attendance'),
    path('summer_club/card', views.card_attendance_summer_club, name='sc_attendance'),

]
