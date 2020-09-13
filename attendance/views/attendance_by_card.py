from django.shortcuts import render, redirect
from attendance.services import AttendanceService
from bank.selectors import CardSelector


def card_attendance_sunday_school(request):
    card_number = request.POST['card_number']
    card = CardSelector().get_card_by_number(card_number)
    AttendanceService().add_attendance_by_card(card=card,
                                               for_sunday_school=True)

    context = {
        'title': 'Sunday School',
    }
    return render(request, 'attendance/attendance.html', context)
