from django.contrib import admin
from .models import Card, Transaction

# Register your models here.


@admin.register(Card)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class UserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
