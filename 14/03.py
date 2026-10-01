a = 10
b = [100, 45, 234]

try:
    print("Start")
    res = b[0] / a
    print("Go")
    raise IndexError("Manually raised IndexError")
except ZeroDivisionError:
    res = 0
except IndexError:
    res = None


print("Result:", res)
