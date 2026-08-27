import copy


a = [5, 7, 12, ["a", "b", "c"], -90]
c = copy.deepcopy(a)

c[3].append("d")

print(a)
print(c)
