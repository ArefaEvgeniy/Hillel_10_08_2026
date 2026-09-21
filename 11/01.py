def func(data=None):
    if data is None:
        data = []
    data.append(len(data))
    return data


print(func([55, 67, 3, 23]))
print(func())
print(func(["56", "FFF"]))
print(func([]))
print(func([33, 456, 7788, 11, 0, 77]))
print(func())
print(func())
print(func(["Hello", "World", 55]))
print(func())
