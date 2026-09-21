def func_1():
    print("Task 1")


def func_2():
    print("Task 2")


def func_3():
    print("Task 3")


def func_4():
    print("Task 4")


def func_5():
    print("Task 5")


def func_incorrect_data():
    print("Invalid input. Please enter a number from 1 to 5.")


# functions = (func_1, func_2, func_3, func_4, func_5)
functions = {"1": func_1, "2": func_2, "3": func_3, "4": func_4, "5": func_5}
while True:
    answer_str = input("Enter a number from 1 to 5: ")
    functions.get(answer_str, func_incorrect_data)()
    # if not answer_str.isdigit():
    #     print("Invalid input. Please enter a number.")
    #     continue
    # answer = int(answer_str)
    # functions[answer - 1]() if 1 <= answer <= 5 else print("Invalid input. Please enter a number from 1 to 5.")
    # if answer == 1:
    #     func_1()
    # elif answer == 2:
    #     func_2()
    # elif answer == 3:
    #     func_3()
    # elif answer == 4:
    #     func_4()
    # elif answer == 5:
    #     func_5()
    # else:
    #     print("Invalid input. Please enter a number from 1 to 5.")
