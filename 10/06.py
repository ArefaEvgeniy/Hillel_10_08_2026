def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        res = func(*args, **kwargs)
        print("After the function call")
        return res
    return wrapper


@decorator  # my_function = decorator(my_function)
def my_function():
    return "I am along function"


@decorator
def function(a, b):
    print("a + b = ", a + b)


print(my_function())
print("----------------------")
function(10, 50)
