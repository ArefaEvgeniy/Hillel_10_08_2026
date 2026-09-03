my_list = ["Привіт", "світ", "Python", "код", 44, 0, -10]
my_tuple = ("Привіт", "світ", "Python", "код", 44, 0, -10)

print(type(my_list))
print(type(my_tuple))

a = [10,]
b = (10,)
print(type(b))

a_1 = [1, 2, 3]
a_2 = [1, 2, 3]

b_1 = (1, 2, 3)
b_2 = (1, 2, 3)

print(id(a_1))
print(id(a_2))
print(id(b_1))
print(id(b_2))
