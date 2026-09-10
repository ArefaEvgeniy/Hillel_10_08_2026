def func_1():
    name = "Bob"
    print(f"Hello, {name}!")
    return name


def func_2():
    def func_3():
        name = "David"
        print(f"Bye, {name}!")

    func_3()
    name = "Charlie"
    print(f"Hi, {name}!")


name = "Alice"
name = func_1()
func_2()
print(f"Goodbye, {name}!")
