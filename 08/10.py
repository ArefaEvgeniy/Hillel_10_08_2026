def func(a: int, b: int = 0, c: str = "") -> bool:
    res = a + b
    print(c, res)
    return c == str(res)


print(func(45, 33, "78"))  # True
print(func.__annotations__)
