from django.shortcuts import render, redirect
from attendance.services import AttendanceService
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from config.selectors.student import StudentSelector
from attendance.selectors.attendance import AttendanceSelector
from django.http import HttpResponse


student_names = StudentSelector().get_all_student_names()


def name_attendance_sunday_school(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

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
        'student_names': student_names,
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_sunday_school=True),
    }
    return render(request, 'attendance/sunday_school.html', context)


def name_attendance_bible_study(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

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
        'student_names': student_names,
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(for_bible_study=True),
    }
    return render(request, 'attendance/bible_study.html', context)


def name_attendance_summer_club(request):

    if not request.user.is_authenticated:
        return redirect('config:login')
    if request.user.username != 'admin':
        return HttpResponse('Unauthorized', status=401)

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
        'student_names': student_names,
        'attendance_count': AttendanceSelector.get_attendance_count_by_day(),
    }
    return render(request, 'attendance/summer_club.html', context)
