from config.selectors.student import StudentSelector


students = StudentSelector().get_all_students()

for student in students:
    if student.grade != 13:
        student.grade += 1
    print(student.grade)
    student.save()
