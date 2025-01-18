import os

input_path = os.path.normpath(os.path.join(__file__, "..", "input.txt"))
# Number of months in 25 years
MONTHS = 25 * 12

students = []

with open(input_path) as file:
    students = file.read().split("\n")
    students.pop(0)
    
    for i, student in enumerate(students):
        students[i] = student.split(" ")

for student in students:
    name = student[0]
    age_years = int(student[1])
    age_months = int(student[2])
    age = age_years * 12 + age_months

    print(name + " " + str(MONTHS - age))