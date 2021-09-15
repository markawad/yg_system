from django.shortcuts import render, redirect
from attendance.services import AttendanceService
from bank.selectors import CardSelector
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from config.selectors.student import StudentSelector


student_names = StudentSelector().get_all_student_names()


def card_attendance_sunday_school(request):
    err, card = '', ''
    card_number = request.POST['card_number']

    try:
        card = CardSelector().get_card_by_number(card_number)
        AttendanceService().add_attendance_by_card(card=card,
                                                   for_sunday_school=True)
    except ObjectDoesNotExist:
        err = 'Card does not exist.'
    except IntegrityError:
        err = f'{str(card.holder)} has already been recorded.'

    context = {
        'err': err,
        'student_names': student_names,
    }
    return render(request, 'attendance/sunday_school.html', context)


def card_attendance_bible_study(request):
    err, card = '', ''
    card_number = request.POST['card_number']

    try:
        card = CardSelector().get_card_by_number(card_number)
        AttendanceService().add_attendance_by_card(card=card,
                                                   for_bible_study=True)
    except ObjectDoesNotExist:
        err = 'Card does not exist.'
    except IntegrityError:
        err = f'{str(card.holder)} has already been recorded.'

    context = {
        'err': err,
        'student_names': student_names,
    }
    return render(request, 'attendance/bible_study.html', context)


def card_attendance_summer_club(request):
    err, card = '', ''
    card_number = request.POST['card_number']

    try:
        card = CardSelector().get_card_by_number(card_number)
        AttendanceService().add_attendance_by_card(card=card)
    except ObjectDoesNotExist:
        err = 'Card does not exist.'
    except IntegrityError:
        err = f'{str(card.holder)} has already been recorded.'

    context = {
        'err': err,
        'student_names': student_names,
    }
    return render(request, 'attendance/summer_club.html', context)
