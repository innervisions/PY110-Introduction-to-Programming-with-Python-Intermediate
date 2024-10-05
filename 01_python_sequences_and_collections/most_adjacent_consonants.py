# Input - List of Strings
# Output - New list with same strings, sorted by highest number of adjacent consonants.

# Explicit Rules
# - Should return a new list.
# - Adjacent consonants ignore whitespace.
# - Two strings that have the same # of adjacent consonants should keep their order.
# Implicit Rules
# - Strings may contain more than one word.
# - Strings may not be empty.
# - Strings may have no adjacent consonants.
# - Strings should be sorted in descending order.
# - Case is not relevant.
# - Single consonants in a string do not affect sort order in
#   comparison to strings with no consonants. Only adjacent
#   consonants affect sort order.
# Questions
# - Do strings always contain multiple words? [No]
#     - Can strings contain a single word? [Yes]
#     - Can strings be empty? [No]
# - Is it possible for a string to contain no adjacent consonants?
#   [Yes]
# - What is meant by "a space between two consonants in adjacent
#   words"? [A consonant that ends one word followed by a consonant
#   that starts a new word are adjacent.]
# - Should the strings be sorted in ascending or descending order?
#   [Descending]
# - Is case important? [No]
# Data Structure - Lists of Strings

# Algorithm
# Sort the given list using the result of a count_adjacent_consonants function.
# count_adjacent_consonants:
#  - Set max adjacent count to 0.
#  - Iterate through string, ignoring whitespace, keeping track of adjacent cononants.
#  - If greater than previous max value, update max value.

def is_consonant(char: str):
    char = char.casefold()
    return char.isalpha() and char not in {'a', 'e', 'i', 'o', 'u'}

def count_adjacent_consonants(string: str):
    adjacents = 0
    max_adjacents = 0
    for idx, char in enumerate(string.replace(' ', '')):
        if is_consonant(char):
            if idx > 0 and is_consonant(string[idx - 1]):
                adjacents = max(2, adjacents + 1)
        else:
            max_adjacents = max(adjacents, max_adjacents)
            adjacents = 0
    return max_adjacents

def sort_by_consonant_count(lst: list):
    new_list = lst.copy()
    new_list.sort(key=count_adjacent_consonants, reverse=True)
    return new_list

my_list = ["aa", "baa", "ccaa", "dddaa"]
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ["can can", "toucan", "batman", "salt pan"]
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ["bar", "car", "far", "jar"]
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ["day", "week", "month", "year"]
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ["xxxa", "xxxx", "xxxb"]
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
