from config.models.alumni import Alumni
from .student import StudentService
from django.utils import timezone


class AlumniService:

    @staticmethod
    def create_alumni(first_name, middle_name, last_name, birth_day, phone):
        curr_year = timezone.datetime.today().year
        return Alumni.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                     birth_day=birth_day, phone=phone, graduation_year=curr_year)

    def student_to_alumni(self, student):
        StudentService.delete(student)
        self.create_alumni(first_name=student.first_name, middle_name=student.middle_name, last_name=student.last_name,
                           birth_day=student.birth_day, phone=student.phone)
