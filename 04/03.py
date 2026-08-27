number = 100

result = 0
while number > 0:
    if number % 3 == 0:
        number -= 1
        continue
    if result > 1000:
        break
    result += number
    number -= 1
else:
    print("Loop finished without break")
print("END")
print(result)
