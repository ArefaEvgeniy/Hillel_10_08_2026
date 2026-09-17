def outer_function(x):
    def inner_function(y):
        print(s)
        return x + y
    s = "Hello, World!"
    return inner_function


closure = outer_function(10)
result = closure(5)
print(result)
