def zero_function():
    print("The number is zero.")


def first_function():
    print("The number is one.")


def second_function():
    print("The number is two.")


def third_function():
    print("The number is three.")


def fourth_function():
    print("The number is four.")


def other_function():
    print("The number is greater than four.")


answers_dict = {"0": zero_function, "1": first_function, "2": second_function,
                "3": third_function, "4": fourth_function}
answer = input("Enter a number: ")
answers_dict.get(answer, other_function)()

# if answer == 0:
#     zero_function()
# elif answer == 1:
#     first_function()
# elif answer == 2:
#     second_function()
# elif answer == 3:
#     third_function()
# elif answer == 4:
#     fourth_function()
# else:
#     print("The number is greater than four.")
