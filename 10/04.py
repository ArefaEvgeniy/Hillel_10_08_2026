def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper


@decorator  # my_function = decorator(my_function)
def my_function():
    print("I am along function")


@decorator
def new_func():
    print("New function")


@decorator
def function():
    print("10 + 20 = ", 10 + 20)


my_function()
print("----------------------")
new_func()
print("----------------------")
function()
