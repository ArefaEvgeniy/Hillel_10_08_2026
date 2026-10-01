a = 0
b = [100, 45, 234]

try:
    print("Start")
    res = b[0] / a
    res += "eert"
    print("Go")
# except (ZeroDivisionError, IndexError):
except ZeroDivisionError:
    res = 0
except IndexError:
    res = None
except LookupError:
    res = -1
except Exception as err:
    res = 1000
    print(f"Exception block, err: {err}")
else:
    print("Else block")
finally:
    print("Finally block")

print("Result:", res)
