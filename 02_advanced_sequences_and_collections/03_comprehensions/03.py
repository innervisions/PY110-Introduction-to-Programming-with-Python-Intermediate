lst = [["b", "c", "a"], [2, 11, -3], ["blue", "black", "green"]]

# result = []
# for sublist in lst:
#     result.append(sorted(sublist, key=str))

# print(result)

result = [sorted(sublist, key=str) for sublist in lst]
print(result)
