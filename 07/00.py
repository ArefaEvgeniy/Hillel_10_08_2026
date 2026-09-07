answer = "y"
while answer == "y" or answer == "yes":
    ...
    answer = input("Do you want to continue? (y(yes)/n): ")


while True:
    ...
    answer = input("Do you want to continue? (y/yes/т/так): ").lower()
    if answer not in ("y", "yes", "т", "так"):
        break
