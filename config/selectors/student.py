from config.models.student import Student


class StudentSelector:

    @staticmethod
    def get_all_student_count():
        return Student.objects.count()

    @staticmethod
    def get_student_by_full_name(full_name):
        first_name = full_name.split(' ')[0]
        middle_name = full_name.split(' ')[1]
        last_name = full_name.split(' ')[2]

        return Student.objects.get(first_name=first_name, middle_name=middle_name, last_name=last_name)

    @staticmethod
    def get_all_student_names():
        return Student.objects.values_list('first_name', 'middle_name', 'last_name')
