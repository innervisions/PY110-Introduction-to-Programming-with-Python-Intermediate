lst = [["b", "c", "a"], [2, 11, -3], ["blue", "black", "green"]]

# result = []
# for sublist in lst:
#     result.append(sorted(sublist))

# print(result)

result = [sorted(sublist) for sublist in lst]
print(result)
