from config.tests.base import BaseTestCase
from django.core.exceptions import ValidationError
from config.services.student import StudentService
from config.selectors.student import StudentSelector
from dateutil.relativedelta import relativedelta
import datetime


class UserTestCase(BaseTestCase):

    def test_adding_user_with_birth_day_less_than_12_years_returns_validation_error(self):
        user_count = StudentSelector.get_all_student_count()
        with self.assertRaisesMessage(ValidationError, 'Year cannot be less than 12 years.'):
            date = str(datetime.date.today() - relativedelta(years=11))
            StudentService().create_student(first_name='Mark',
                                            middle_name='Smithy',
                                            last_name='Smith',
                                            birth_day=date,
                                            phone=12345678,
                                            grade=9,
                                            school='asdavfs',
                                            mothers_number=113123,
                                            fathers_number=123123,
                                            father_of_confession='Father',
                                            servant=self.servant,
                                            residency_area='Prague')
        new_user_count = StudentSelector.get_all_student_count()
        self.assertEqual(user_count, new_user_count)
