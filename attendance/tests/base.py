from django.test import TestCase
from bank.services.card import CardService
from config.models import Student, Servant
from attendance.services.day import DayService
from config.models.bonus import Bonus
from freezegun import freeze_time
import datetime


class BaseTestCase(TestCase):

    def setUp(self):
        DayService().add_attendance_day(for_sunday_school=True)
        DayService().add_attendance_day(for_bible_study=True)

        self.servant = Servant.objects.create(first_name='John',
                                              middle_name='Smithy',
                                              last_name='Smith',
                                              birth_day='1996-04-05',
                                              phone=12345678)
        self.student1 = Student.objects.create(first_name='Mark',
                                               middle_name='Smithy',
                                               last_name='Smith',
                                               birth_day='1996-04-05',
                                               phone=12345678,
                                               grade=9,
                                               school='asdavfs',
                                               mothers_number=113123,
                                               fathers_number=123123,
                                               father_of_confession='Father',
                                               servant=self.servant,
                                               residency_area='Prague')
        self.student2 = Student.objects.create(first_name='Dani',
                                               middle_name='Smithy',
                                               last_name='Smith',
                                               birth_day='1996-04-05',
                                               phone=12345678,
                                               grade=9,
                                               school='asdavfs',
                                               mothers_number=113123,
                                               fathers_number=123123,
                                               father_of_confession='Father',
                                               servant=self.servant,
                                               residency_area='Prague')
        self.card1 = CardService().create_card(self.student1, number=1234)
        self.card2 = CardService().create_card(self.student2, number=1222)

        Bonus.objects.create(WEEK=5, MONTH=10, QUARTER=25)

    @staticmethod
    def func_with_different_date(increment, func):
        @freeze_time(datetime.date.today() + datetime.timedelta(days=increment))
        def function(func):
            return func()

        function(func)
