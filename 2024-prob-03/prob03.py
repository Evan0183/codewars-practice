# Read input from the file
lines = []

with open("2024-prob-03/input.txt") as file:
    lines = file.read().split("\n")

    for i, line in enumerate(lines):
        if line == "-1":
            lines.pop(i)

# Print for every line of input
for line in lines:
    num = int(line)
    word = "minute"

    # Unless the number is 1, make the word plural
    if num != 1:
        word += "s"
    
    # Print the line with the number and the word
    print("You, " + str(num) + " " + word + " ago.")