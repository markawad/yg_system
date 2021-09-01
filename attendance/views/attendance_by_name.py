from django.shortcuts import render, redirect
from attendance.services import AttendanceService
from bank.selectors import CardSelector
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from config.selectors.student import StudentSelector


def name_attendance_sunday_school(request):
    err, student = '', ''
    full_name = request.POST['full_name']

    try:
        student = StudentSelector.get_student_by_full_name(full_name)
        AttendanceService().add_attendance_by_student(student, for_sunday_school=True)
    except ObjectDoesNotExist:
        err = 'Name does not exist.'
    except IntegrityError:
        err = f'{str(student)} has already been recorded.'

    context = {
        'err': err,
    }
    return render(request, 'attendance/sunday_school.html', context)


def name_attendance_bible_study(request):
    err, student = '', ''
    full_name = request.POST['full_name']

    try:
        student = StudentSelector.get_student_by_full_name(full_name)
        AttendanceService().add_attendance_by_student(student, for_bible_study=True)
    except ObjectDoesNotExist:
        err = 'Name does not exist.'
    except IntegrityError:
        err = f'{str(student)} has already been recorded.'

    context = {
        'err': err,
    }
    return render(request, 'attendance/bible_study.html', context)


def name_attendance_summer_club(request):
    err, student = '', ''
    full_name = request.POST['full_name']

    try:
        student = StudentSelector.get_student_by_full_name(full_name)
        AttendanceService().add_attendance_by_student(student)
    except ObjectDoesNotExist:
        err = 'Name does not exist.'
    except IntegrityError:
        err = f'{str(student)} has already been recorded.'

    context = {
        'err': err,
    }
    return render(request, 'attendance/summer_club.html', context)
