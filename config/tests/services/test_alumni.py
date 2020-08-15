from config.tests.base import BaseTestCase
from config.services.alumni import AlumniService
from config.selectors.alumni import AlumniSelector
from config.selectors.student import StudentSelector


class AlumniTestCase(BaseTestCase):

    def test_new_alumni_no_longer_student(self):
        student_count = StudentSelector.get_all_student_count()
        alumni_count = AlumniSelector.get_all_alumni_count()

        AlumniService().student_to_alumni(student=self.student)

        new_student_count = StudentSelector.get_all_student_count()
        new_alumni_count = AlumniSelector.get_all_alumni_count()

        self.assertEqual(student_count, new_student_count + 1)
        self.assertEqual(alumni_count + 1, new_alumni_count)
