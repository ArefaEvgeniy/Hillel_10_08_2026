a = [5, 7, 12, -90]
b = a.copy()
c = a[:]

import copy
d = copy.copy(a)

a.pop()

print(a)
print(b)
print(c)
print(d)
