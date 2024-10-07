def double_numbers(numbers):
    for idx in range(len(numbers)):
        numbers[idx] *= 2
    return numbers


numbers = [1, 2, 3, 4, 5]
double_numbers(numbers)
print(numbers)
