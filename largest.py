def find_largest_num(input_list):
    largest_num = 0
    for num in input_list:
        if num > largest_num:
            largest_num = num
    return largest_num


print(find_largest_num([4, 2, 0, 33, 1, 8, 3, 15]))
