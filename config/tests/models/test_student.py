from config.tests.base import BaseTestCase
from config.models import Student


class StudentTestCase(BaseTestCase):

    def test_printing_student_displays_full_name(self):
        self.assertEqual(str(self.student), 'Mark Smithy Smith')

    def test_grade_displayed_in_proper_format(self):
        self.assertEqual(self.student.get_grade_display(), 'Grade 9')

    def test_student_still_exists_after_servant_is_deleted(self):
        student_count = Student.objects.count()
        student = self.servant.students.first()
        self.servant.delete()
        new_student_count = Student.objects.count()
        query = Student.objects.filter(id=student.id).count()
        self.assertEqual(student_count, new_student_count)
        self.assertEqual(query, 1)
