from attendance.models.multiplier import Multiplier
from django.db import IntegrityError


class MultiplierService:

    def increment_multiplier(self, student, sunday_school=False, bible_study=False):
        multiplier = self.get_or_create_multiplier(student=student)
        if sunday_school:
            multiplier.sunday_school += 1
        if bible_study:
            multiplier.bible_study += 1
        if not sunday_school and not bible_study:
            multiplier.summer_club += 1
        multiplier.save()

    @staticmethod
    def get_or_create_multiplier(student):
        return Multiplier.objects.get_or_create(student=student)[0]

    def reset_multiplier(self, student, sunday_school=False, bible_study=False):
        multiplier = self.get_or_create_multiplier(student)
        if sunday_school:
            multiplier.sunday_school = 0
        if bible_study:
            multiplier.bible_study = 0
        if not sunday_school and not bible_study:
            multiplier.summer_club = 0
        multiplier.save()
