
my_set = {'a', 'b', 'c'}
new_set = frozenset(my_set)
a = {1, 2, new_set, 3, 4}

print(a)
