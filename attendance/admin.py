from django.contrib import admin
from .models import Attendance, Day, Multiplier, StartYear

# Register your models here.


@admin.register(Attendance)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Day)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Multiplier)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(StartYear)
class UserAdmin(admin.ModelAdmin):
    pass