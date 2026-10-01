def func(a, b):
    try:
        print("Start")
        res = b[2] / a
        res += "eert"
        print("Go")
    except ZeroDivisionError:
        res = 0
    except IndexError:
        res = None

    print("End function")
    return res


a = 10
b = [100, 45, 234]
try:
    result = func(a, b)
except TypeError:
    result = "TypeError occurred"

print("Result:", result)
