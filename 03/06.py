age = input("Please enter your age: ")

if not age.isdigit() or int(age) <= 0:
    print("Wrong input. Age cannot be negative.")
elif int(age) < 10:
    print("Milk")
elif int(age) < 18:
    print("Juice")
elif int(age) < 60:
    print("Beer")
elif int(age) < 120:
    print("Tea")
else:
    print("Wrong input. Age cannot be greater than 120.")
