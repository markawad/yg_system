from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Student, Servant, Alumni, Discount, Bonus
from bank.models import Card

# Register your models here.


class CardInline(admin.StackedInline):
    model = Card


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (CardInline,)


@admin.register(Servant)
class ServantAdmin(admin.ModelAdmin):
    pass


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request, obj=None):
    #     return False
    pass


# @admin.register(Discount)
# class DiscountAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request, obj=None):
#         return False


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False


admin.site.unregister(User)
admin.site.unregister(Group)