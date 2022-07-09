from config.models.student import Student
from django.db.models import Value as V
from django.db.models.functions import Concat


class StudentSelector:

    @staticmethod
    def get_all_student_count():
        return Student.objects.count()

    @staticmethod
    def get_student_by_full_name(full_name):
        return Student.objects.annotate(full_name=Concat('first_name', V(' '), 'middle_name', V(' '), 'last_name')).\
            filter(full_name__icontains=full_name).get()

    @staticmethod
    def get_all_student_names():
        return [student.first_name + " " + student.middle_name + " " + student.last_name
                for student in Student.objects.all()]

    @staticmethod
    def get_all_students():
        return Student.objects.all()
