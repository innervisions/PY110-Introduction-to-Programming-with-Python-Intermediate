def odd_sum(numbers):
    return sum([num for num in numbers if num % 2])

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
new_lst = sorted(lst, key=odd_sum)
print(new_lst)
