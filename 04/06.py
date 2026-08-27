my_list = [3, 55, "45", 0, "werr", 23, 12, 45, -230, 99]

new_list = []
index_list = []
for index, value in enumerate(my_list):
    if type(value) == str:
        new_list.append(value)
        index_list.append(index)

print(new_list)
print(index_list)
