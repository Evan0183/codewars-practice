MONTHS = 25 * 12

students = []

with open("2024-prob-06/input.txt") as file:
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