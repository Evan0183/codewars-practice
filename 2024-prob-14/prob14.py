def get_num_decimal_places(number):
    decimal_places = 0

    if "." in number:
        decimal_places = len(number) - number.index(".") - 1

    return decimal_places

data = []
check_sum = 0

with open("2024-prob-14/input.txt") as file:
    lines = file.read().split("\n")
    data = lines[0].split(" ")
    check_sum = lines[1][9:]

numeric_data = []

for value in data:
    try:
        number = float(value)
        numeric_data.append(value)
    except ValueError:
        pass

max_decimal_places = 0

for value in numeric_data:
    decimal_places = get_num_decimal_places(value)

    if decimal_places > max_decimal_places:
        max_decimal_places = decimal_places

for i, value in enumerate(numeric_data):
    if i == len(numeric_data) - 1:
        print(value)
    else:
        print(value, end=" ")

actual_sum = 0

for value in numeric_data:
    actual_sum += float(value)

actual_sum = str(actual_sum)
sum_decimal_places = get_num_decimal_places(actual_sum)

if sum_decimal_places < max_decimal_places:
    difference = max_decimal_places - sum_decimal_places
    actual_sum += "0" * difference
elif sum_decimal_places > max_decimal_places:
    difference = sum_decimal_places - max_decimal_places
    actual_sum = actual_sum[:-difference - 1]

if actual_sum == check_sum:
    print("CHECKED")
else:
    print("BADCHECK:" + str(actual_sum))