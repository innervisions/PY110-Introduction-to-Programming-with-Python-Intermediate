def double_odd_indexes(numbers):
    new_numbers = []
    for idx, number in enumerate(numbers):
        if idx % 2:
            new_numbers.append(number * 2)
        else:
            new_numbers.append(number)
    return new_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_indexes(my_numbers))
