def func_1():
    print("Hello, World!")


def func_2(f):
    f()


def func_3():
    def func_4():
        print("Goodbye, World!")

    return func_4


a = 10
print(func_1)
a = func_1
a()
func_1 = 100
print(func_1)
del func_1
a()
print(a)
print("------")
func_2(a)

b = func_3()
b()
