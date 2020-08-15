from attendance.models.attendance import Attendance
from attendance.selectors.day import DaySelector
from .multiplier import MultiplierService
from attendance.selectors.multiplier import MultiplierSelector
from .day import DayService
from bank.services.card import CardService
from config.selectors.bonus import BonusSelector
from django.utils import timezone


class AttendanceService:

    def add_attendance(self, card_holder, sunday_school=False, bible_study=False):
        day = DayService().add_attendance_day(for_sunday_school=sunday_school, for_bible_study=bible_study)
        self.reset_multiplier_if_absent_last_time(student=card_holder,
                                                  sunday_school=sunday_school,
                                                  bible_study=bible_study)
        MultiplierService().increment_multiplier(student=card_holder,
                                                 sunday_school=sunday_school,
                                                 bible_study=bible_study)
        Attendance.objects.create(student=card_holder, day=day)

    def add_attendance_by_card(self, card, for_sunday_school=False, for_bible_study=False):
        self.add_attendance(card_holder=card.holder, sunday_school=for_sunday_school, bible_study=for_bible_study)
        multiplier = MultiplierSelector().get_multiplier_for_specific_service_value(card.holder,
                                                                                    sunday_school=for_sunday_school,
                                                                                    bible_study=for_bible_study)
        if multiplier % 12 == 0:
            bonus = BonusSelector().get_quarterly_bonus()
        elif multiplier % 4 == 0:
            bonus = BonusSelector().get_monthly_bonus()
        else:
            bonus = BonusSelector().get_weekly_bonus()
        CardService().add_attendance_bonus(card=card, amount=bonus)

    def add_attendance_by_student(self, student, for_sunday_school=False, for_bible_study=False):
        self.add_attendance(card_holder=student, sunday_school=for_sunday_school, bible_study=for_bible_study)

    @staticmethod
    def student_was_present_last_time(student, date):
        return Attendance.objects.filter(student=student, day=date).count()

    def reset_multiplier_if_absent_last_time(self, student, sunday_school, bible_study):
        date = DaySelector().get_date_of_last_time(for_sunday_school=sunday_school, for_bible_study=bible_study)
        if date:
            if not self.student_was_present_last_time(student, date):
                MultiplierService().reset_multiplier(student, sunday_school=sunday_school, bible_study=bible_study)
