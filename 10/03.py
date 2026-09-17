def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper


@decorator  # my_function = decorator(my_function)
def my_function():
    print("I am along function")


my_function()
