my_list = [1, 2, 0, -100, [0, 99, "TT"], "rr", "tyy", True]

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

my_list.pop()
print(my_list)
print(id(my_list))
