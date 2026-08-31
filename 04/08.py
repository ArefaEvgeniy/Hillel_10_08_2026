my_list = [3, 66, -40, 34, 0, 99, -77, 23, 12, 45, -230, 99]

new_list = []
for value in my_list:
    new_list.append(value * 2)

print(new_list)

new_list_2 = [value * 2 for value in my_list]
print(new_list_2)
