from django.shortcuts import render, redirect
from attendance.services import AttendanceService
from bank.selectors import CardSelector
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from config.selectors.student import StudentSelector
from attendance.selectors.attendance import AttendanceSelector
from django.http import HttpResponse


def card_attendance_sunday_school(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

    err, card = '', ''
    card_number = request.POST['card_number']
    student_names = StudentSelector().get_all_student_names()

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
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_sunday_school=True),
    }
    return render(request, 'attendance/sunday_school.html', context)


def card_attendance_bible_study(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

    err, card = '', ''
    card_number = request.POST['card_number']
    student_names = StudentSelector().get_all_student_names()

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
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_bible_study=True),
    }
    return render(request, 'attendance/bible_study.html', context)


def card_attendance_summer_club(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

    err, card = '', ''
    card_number = request.POST['card_number']
    student_names = StudentSelector().get_all_student_names()

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
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(),
    }
    return render(request, 'attendance/summer_club.html', context)
