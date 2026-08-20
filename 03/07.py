a = 10
b = None

if a > 0:
    print("a is positive")
    b = 1
elif a == 0:
    print("a is zero")
    b = False
else:
    print("a is negative")
    b = 0


print("a is positive") if a > 0 else (print("a is zero") if a == 0 else print("a is negative"))

c = 1 if a > 0 else 0

print("b:", b)
print("c:", c)
