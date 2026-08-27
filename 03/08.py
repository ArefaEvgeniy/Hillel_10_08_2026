my_list = [1, 2, 0, -100, [0, 99, "TT"], "rr", -100, "tyy", -100, True]

print(len(my_list))

print("rr" in my_list)
print("AAA" in my_list)
print("TT" in my_list)

print(list("RRETTFG"))
print(list((10,)))

a = [10,]

print(a)

print(id(my_list))
my_list.append(101)
print(my_list)
print(id(my_list))

new = my_list.pop()
print(my_list)
print(id(my_list))
print(new)

a = 10
a += 2

if len(my_list) > 12:
    new_2 = my_list.pop(12)
    print(my_list)
    print(new_2)

if -1000 in my_list:
    my_list.remove(-1000)
    print(my_list)

print(my_list[4][1])

my_list.remove(-100)
print(my_list)

my_list.remove(-100)
print(my_list)
