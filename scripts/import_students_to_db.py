from config.services.student import StudentService
from bank.services.card import CardService
import csv

file_name = ''

with open(file_name, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

for record in data:

    record[5] = '01/01/1990' if record[5] == 'NA' else record[5]
    record[7] = '00000000' if record[7] == 'NA' else record[7]
    record[8] = '00000000' if record[8] == 'NA' else record[8]
    record[9] = '00000000' if record[9] == 'NA' else record[9]
    print(record[0], record)
    date = record[5]

    student = StudentService().create_student(first_name=record[1], middle_name=record[2], last_name=record[3],
                                    grade=int(record[4]), mothers_number=record[9], fathers_number=record[8],
                                    phone=record[7], school=record[6], father_of_confession=record[10],
                                    residency_area=record[11], servant=None, birth_day=date)

    CardService().create_card(holder=student, number=int(record[0]))
    print(student.first_name)