import os

input_path = os.path.normpath(os.path.join(__file__, "..", "input.txt"))
# Read input from the file
lines = []

with open(input_path) as file:
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