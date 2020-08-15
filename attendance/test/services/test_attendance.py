from attendance.test.base import BaseTestCase
from attendance.services import DayService, AttendanceService
from attendance.selectors.multiplier import MultiplierSelector
from django.db import IntegrityError
from config.selectors.bonus import BonusSelector


class AttendanceTestCase(BaseTestCase):

    def test_adding_same_student_to_attendance_returns_integrity_error(self):
        AttendanceService().add_attendance_by_card(card=self.card1, for_sunday_school=True)
        with self.assertRaises(IntegrityError):
            AttendanceService().add_attendance_by_card(card=self.card1, for_sunday_school=True)

    def test_adding_attendance_for_student_increases_their_multiplier(self):
        AttendanceService().add_attendance_by_card(card=self.card1, for_sunday_school=True)
        AttendanceService().add_attendance_by_card(card=self.card1, for_bible_study=True)
        AttendanceService().add_attendance_by_card(card=self.card1)

        multiplier = MultiplierSelector().get_multiplier(student=self.card1.holder)
        self.assertEqual(multiplier.sunday_school, 1)
        self.assertEqual(multiplier.bible_study, 1)
        self.assertEqual(multiplier.summer_club, 1)

    def test_student_loses_multiplier_bonus_after_skipping_a_day(self):
        # Day 1: increment multiplier
        add_attendance = lambda card: AttendanceService().add_attendance_by_card(card, for_sunday_school=True)
        add_attendance(self.card1)

        # Day 2: no attendance
        self.func_with_different_date(1, lambda: DayService().add_attendance_day(for_sunday_school=True))

        # Day 3: consecutive attendance should equal 1
        self.func_with_different_date(2, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                            for_sunday_school=True))

        multiplier = MultiplierSelector().get_multiplier(self.card1.holder)
        self.assertEqual(multiplier.sunday_school, 1)

    def test_student_skips_a_service_but_multiplier_stays_the_same_in_other_services(self):

        # Day 1: add attendance for sunday school and for bible study
        AttendanceService().add_attendance_by_card(self.card1, for_bible_study=True)
        AttendanceService().add_attendance_by_card(self.card1, for_sunday_school=True)

        # Day 2: The person skipped sunday school
        self.func_with_different_date(1, lambda: DayService().add_attendance_day(for_sunday_school=True))
        self.func_with_different_date(1, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                            for_bible_study=True))

        # Day 3: Person came for both services
        self.func_with_different_date(2, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                            for_sunday_school=True))
        self.func_with_different_date(2, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                            for_bible_study=True))

        multiplier = MultiplierSelector().get_multiplier(self.card1.holder)
        self.assertEqual(multiplier.sunday_school, 1)
        self.assertEqual(multiplier.bible_study, 3)

    def test_when_a_student_is_added_by_name_multiplier_is_incremented(self):
        AttendanceService().add_attendance_by_student(self.card1.holder, for_sunday_school=True)
        multiplier = MultiplierSelector().get_multiplier(self.card1.holder)

        self.assertEqual(multiplier.sunday_school, 1)

    def test_money_is_added_as_bonus_for_attendance_with_card(self):
        AttendanceService().add_attendance_by_card(self.card1, for_sunday_school=True)
        bonus = BonusSelector().get_weekly_bonus()
        self.assertEqual(self.card1.balance, bonus)

    def test_bonus_added_correctly_for_monthly_and_quarterly_multiplier(self):
        # Pass one month
        for i in range(1, 5):
            self.func_with_different_date(i, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                                for_sunday_school=True))
        bonus = BonusSelector().get_bonus_values()
        monthly_value = bonus.WEEK * 3 + bonus.MONTH
        self.assertEqual(monthly_value, self.card1.balance)

        # Pass two more months for the quarter
        for i in range(5, 13):
            self.func_with_different_date(i, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                                for_sunday_school=True))
        quarter_value = bonus.WEEK * 9 + bonus.MONTH * 2 + bonus.QUARTER * 1
        self.assertEqual(quarter_value, self.card1.balance)

    def test_multiplier_adds_bonus_for_different_services_independently(self):
        for i in range(1, 4):
            self.func_with_different_date(i, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                                for_sunday_school=True))
        self.func_with_different_date(1, lambda: AttendanceService().add_attendance_by_card(self.card1,
                                                                                            for_bible_study=True))
        # 3 weeks for sunday school, 1 week for bible study and NOT monthly bonus for sunday school
        bonus_value = BonusSelector().get_weekly_bonus() * 4
        self.assertEqual(bonus_value, self.card1.balance)

    def test_no_money_is_added_when_student_has_attendance_by_name(self):
        AttendanceService().add_attendance_by_student(self.card1.holder, for_sunday_school=True)
        self.assertEqual(self.card1.balance, 0)

    def test_transaction_recorded_when_attendance_money_is_added(self):
        AttendanceService().add_attendance_by_card(self.card1)
        self.assertEqual(self.card1.transactions.count(), 1)
