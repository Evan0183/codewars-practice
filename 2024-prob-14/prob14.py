data = []
check_sum = 0

with open("2024-prob-14/input.txt") as file:
    lines = file.read().split("\n")
    data = lines[0].split(" ")
    check_sum = lines[1][9:]

print(lines)
print(check_sum)