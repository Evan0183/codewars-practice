import os

input_path = os.path.normpath(os.path.join(__file__, "..", "input.txt"))
# A list of all of the words in the input file, in order
words = []
# A list of all vowels
VOWELS = ["a", "e", "i", "o", "u"]

with open(input_path) as file:
    for word in file.read().strip().split("\n"):
        word = word.strip()

        if word == "z":
            break

        words.append(word)

def is_sorted(string):
    """
    Determines if the string is sorted in alphabetical order.

    Returns True if string is sorted in alphabetical order as defined by the 
    sorted method, returns False otherwise.
    """

    return string == "".join(sorted(string))

def filter_characters(string, chars, include):
    """
    Filters a string to only include or exclude a given set of characters.

    If include is True, the returned string will be the given string with all 
    characters that are not in the chars list removed.

    If include is False, the returned string will be the given string with 
    all characters that are in the chars list removed.
    """

    result_string = ""

    for char in string:
        if (char in chars and include) or (not char in chars and not include):
            result_string += char
    
    return result_string

for word in words:
    sort_grade = ""

    if is_sorted(word):
        sort_grade = "SORTED"
    