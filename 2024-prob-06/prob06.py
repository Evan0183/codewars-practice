import os

input_path = os.path.normpath(os.path.join(__file__, "..", "input.txt"))
# Number of months in 25 years
MONTHS = 25 * 12

# Stores data for each student. Each student's data includes the student's 
# name, age in years, and age in months.
students = []

# Read in the student data
with open(input_path) as file:
    students = file.read().split("\n")
    # Remove the first line of input, which is the number of students
    students.pop(0)
    
    # For each student, split their data by spaces
    for i, student in enumerate(students):
        students[i] = student.split(" ")

# Determine the number of months before each student is 25 years old
for student in students:
    name = student[0]
    age_years = int(student[1])
    age_months = int(student[2])
    # Calculate the student's age in months
    age = age_years * 12 + age_months

    # Print the student's name and the number of months before they become 25 
    # years old
    print(name + " " + str(MONTHS - age))