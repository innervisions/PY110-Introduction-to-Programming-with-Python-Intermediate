def multiply(numbers, term):
    products = []
    for num in my_numbers:
        products.append(num * term)

    return products

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]
