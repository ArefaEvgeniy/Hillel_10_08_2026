def func(a, b):
    if a > b:
        return a - b
    else:
        return a + b


func_2 = lambda a, b: a - b if a > b else a + b
func_3 = lambda: print("Hello, World!")

print(func(30, 20))
print((lambda a, b: a + b)(10, 20))
print(func_2(30, 20))
func_3()
