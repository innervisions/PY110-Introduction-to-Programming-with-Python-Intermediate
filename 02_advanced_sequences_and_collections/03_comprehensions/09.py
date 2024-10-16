def all_even(dictionary):
    for numbers in dictionary.values():
       if any(number % 2 != 0 for number in numbers) :
        return False
    return True

lst = [
    {"a": [1, 2, 3]},
    {"b": [2, 4, 6], "c": [3, 6], "d": [4]},
    {"e": [8], "f": [6, 10]},
]

new_lst = [dictionary for dictionary in lst if all_even(dictionary)]
print(new_lst)
