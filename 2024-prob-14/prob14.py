import os

input_path = os.path.normpath(os.path.join(__file__, "..", "input.txt"))

def get_num_decimal_places(number):
    """
    Returns the number of decimal places in number.

    Precondition: number is a valid decimal number represented as a string, 
    meaning that it can only include up to one hyphen ("-") at the start, up 
    to one decimal point (".") after any hyphen, and at least one decimal 
    digit after any hyphen.
    Postcondition: the number of digits which appear after the decimal point, 
    not including the decimal point, is returned. If there is no decimal 
    point, 0 is returned.

    number: decimal number to count the number of decimal places of
    """
    decimal_places = 0

    # Check that there is a decimal point in number before finding the index
    if "." in number:
        decimal_places = len(number) - number.index(".") - 1

    return decimal_places

# List of all the space-separated values of the first line of input
data = []
# Check sum value in the second line of input
check_sum = 0

with open(input_path) as file:
    lines = file.read().split("\n")
    # Get the data from the first line
    data = lines[0].split(" ")
    # Get the check sum from the second line
    check_sum = lines[1][9:]

# Contains only the elements of data that are valid floats
numeric_data = []

# Check each element in data for validity as a float
for value in data:
    try:
        # If the float function runs without error, value is a valid float
        number = float(value)
        numeric_data.append(value)
    except ValueError:
        pass

# The number of decimal places of the element in numeric_data with the 
# greatest number of decimal places
max_decimal_places = 0

for value in numeric_data:
    decimal_places = get_num_decimal_places(value)

    # If this value has more decimal places than max_decimal_places, update 
    # max_decimal_places
    if decimal_places > max_decimal_places:
        max_decimal_places = decimal_places

# Print the elements of numeric_data on one line
for i, value in enumerate(numeric_data):
    # Only create a new line if this is the last element. Otherwise, follow 
    # the value with a space
    if i == len(numeric_data) - 1:
        print(value)
    else:
        print(value, end=" ")

# Find the sum of all numbers in numeric_data
actual_sum = 0

for value in numeric_data:
    actual_sum += float(value)

# actual_sum must have the same number of decimal places as the element in 
# numeric_data with the most decimal places, so convert actual_sum to a 
# string so that any trailing zeroes are preserved and any additional zero 
# can be removed.
actual_sum = str(actual_sum)
sum_decimal_places = get_num_decimal_places(actual_sum)

# If the sum has fewer decimal places than max_decimal_places, add zeroes to 
# the end of actual_sum. This can happen when data values are summed and 
# result in trailing zeroes, which are removed.
if sum_decimal_places < max_decimal_places:
    difference = max_decimal_places - sum_decimal_places
    actual_sum += "0" * difference
# If the sum has more decimal places than max_decimal_places, remove the 
# additional decimal places. This can happen when data values are all 
# integers and therefore result in an integer sum, which would be represented 
# as a float with a .0 at the end.
elif sum_decimal_places > max_decimal_places:
    difference = sum_decimal_places - max_decimal_places
    actual_sum = actual_sum[:-difference - 1]

# Check that the actual sum and the check sum are equal
if actual_sum == check_sum:
    print("CHECKED")
else:
    print("BADCHECK:" + str(actual_sum))