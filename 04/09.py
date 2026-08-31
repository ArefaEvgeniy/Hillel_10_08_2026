my_list = [3, 66, -40, 34, 0, 99, -77, 23, 12, 45, -230, 99]

new_list = []
for value in my_list:
    if value > 0:
        if value % 2 == 0:
            new_list.append(value * 2)
        else:
            new_list.append(value ** 2)

print(new_list)

new_list_2 = [value * 2 if value % 2 == 0 else value ** 2 for value in my_list if value > 0]
print(new_list_2)

new_list_3 = [True for value in my_list if True]
print(new_list_3)

print([value * 2 for value in my_list if value > 0])
print(tuple([value * 2 for value in my_list if value > 0]))
print({value * 2 for value in my_list if value > 0})
print({value * 2: value ** 2 for value in my_list if value > 0})
