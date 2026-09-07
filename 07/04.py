my_list = [2, "ERT", "34", 3, "ERT", 0, -20, 34.55, "34", 0, "ERT", 99, 0, 12, "ERT", "34", "RRR", "ERT", "34"]

new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

new_list_2 = list(set(my_list))
print(new_list_2)
