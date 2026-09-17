def func_1(*args):
    if len(args) == 0:
        pass


def func_2():
    result = None
    ...
    if result == True:
        return True
    else:
        return False


def func_3(seconds):

    hours = ...
    minutes = ...
    seconds = ...


def func_4(number_):
    for i in range(100):
        if number_ <= 9:
            break
        res = 1
        for digit in str(number_):
            res *= int(digit)
        number_ = res
    print(number_)
    return number_




def func_1(*args):
    if not args:
        pass


def func_2():
    result = None
    ...
    return result


def func_3(input_seconds):

    hours = ...
    minutes = ...
    seconds = ...


def func_4(number):  # 882 -> 128 -> 16 -> 6
    while True:
        if number <= 9:
            break
        res = 1
        for digit in str(number):
            res *= int(digit)
        number = res
    print(number)
    return number
