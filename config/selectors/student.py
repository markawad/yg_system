from config.models.student import Student


class StudentSelector:

    @staticmethod
    def get_all_student_count():
        return Student.objects.count()
