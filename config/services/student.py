from config.models.student import Student
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from django.db import models


class StudentService:

    def create_student(self, first_name: str, middle_name: str, last_name: str, birth_day: str, phone: int, grade: int,
                       school: str, fathers_number: int, mothers_number: int, father_of_confession: str,
                       servant: str, residency_area: str) -> models.Model:
        self.validate_date(birth_day=birth_day)
        return Student.objects.create(first_name=first_name,
                                      middle_name=middle_name,
                                      last_name=last_name,
                                      birth_day=birth_day,
                                      phone=phone,
                                      grade=grade,
                                      school=school,
                                      fathers_number=fathers_number,
                                      mothers_number=mothers_number,
                                      father_of_confession=father_of_confession,
                                      servant=servant,
                                      residency_area=residency_area)

    @staticmethod
    def validate_date(birth_day):
        if timezone.datetime.today().year - parse_date(birth_day).year < 12:
            raise ValidationError('Year cannot be less than 12 years.')

    @staticmethod
    def delete(student):
        student.delete()
