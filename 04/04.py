my_list = [3, 55, "45", 0, "werr", 23, 12, 45, -230, 99]

result = 0
index = 0
while index < len(my_list):
    if type(my_list[index]) == int:
        result += my_list[index]
    index += 1
print(result)

result_2 = 0
for item in my_list:
    if type(item) == int:
        if item < 0:
            continue
        result_2 += item
        if result_2 > 100:
            break
else:
    print("Loop finished without break")
print(result_2)
