data = []
check_sum = 0

with open("2024-prob-14/input.txt") as file:
    lines = file.read().split("\n")
    data = lines[0].split(" ")
    check_sum = float(lines[1][9:])

numeric_data = []

for value in data:
    try:
        number = float(value)
        numeric_data.append(value)
    except ValueError:
        pass

for i, value in enumerate(numeric_data):
    if i == len(numeric_data) - 1:
        print(value)
    else:
        print(value, end=" ")

actual_sum = 0

for value in numeric_data:
    actual_sum += float(value)

if actual_sum == check_sum:
    print("CHECKED")
else:
    print("BADCHECK:" + str(actual_sum))