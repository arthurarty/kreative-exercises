max_three = lambda x, y, z: max(x, y, z)
print(max_three(45, 32, 89))


list_a = [2, 4, 5, 8]
list_b = [4, 8, 12, 16]
common = list(filter((lambda item: item in list_b), list_a))
print(common)
