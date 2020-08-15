from attendance.models import Multiplier
from django.core.exceptions import ObjectDoesNotExist


class MultiplierSelector:

    @staticmethod
    def get_multiplier(student):
        try:
            return Multiplier.objects.get(student=student)
        except ObjectDoesNotExist:
            return Multiplier.objects.create(student=student)

    @staticmethod
    def get_multiplier_for_specific_service_value(student, sunday_school=False, bible_study=False):
        multiplier = Multiplier.objects.get_or_create(student=student)[0]
        if sunday_school:
            return multiplier.sunday_school
        if bible_study:
            return multiplier.bible_study
        return multiplier.summer_club
