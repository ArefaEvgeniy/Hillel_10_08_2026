def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(10))  # Output: 1
print(factorial(996))


def factorial_2(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(factorial_2(5))
print(factorial_2(996))
print(factorial_2(1500))
