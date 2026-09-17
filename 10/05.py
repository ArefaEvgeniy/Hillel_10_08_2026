def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")
    return wrapper


@decorator  # my_function = decorator(my_function)
def my_function():
    print("I am along function")


@decorator
def function(a, b):
    print("a + b = ", a + b)


my_function()
print("----------------------")
function(10, 50)
