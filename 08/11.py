def func(a, b, c):
    """
    This function takes three parameters a, b, and c.
    It calculates the sum of a and b, prints the value of c along with the result,
    and returns True if c is equal to the string representation of the sum,
    otherwise it returns False.
    :param a: owner money
    :param b: bill money
    :param c: person money
    :return: enough money or not
    >>> func(45, 33, "78")
    >>> True
    >>> func(45, 33, "77")
    >>> False
    """
    res = a + b
    print(c, res)
    return c == str(res)


print(func(45, 33, "78"))  # True
print(func.__doc__)
