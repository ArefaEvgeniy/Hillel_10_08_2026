def func_1(item: int):
    if item < 0:
        return abs(item)
    else:
        return item * 2


my_list = [-10, 0, 5, 20, -3, 7]
print(list(map(func_1, my_list)))
print(list(map(lambda item: abs(item) if item < 0 else item * 2, my_list)))


