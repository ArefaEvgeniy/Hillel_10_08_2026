def func(item: int):
    if item <= 0:
        return abs(item) * 2
    else:
        return True


my_list = [-10, 0, 5, 20, -3, 7]
print(list(filter(func, my_list)))
