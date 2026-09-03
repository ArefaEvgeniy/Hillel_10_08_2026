from collections import defaultdict


dct = defaultdict(lambda: 0)
dct.update({"ee": 556, "rr": 556, "tt": 556})

print(dct)
print(dct["ee"])
print(dct["aa"])
print(dct)
