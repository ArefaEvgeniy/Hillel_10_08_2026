names = ['Alice', 'Bob', 'Charlie', 'Diana']
ages = [25, 30, 22, 66, 34, 78]
phone_numbers = ['123-456-7890', '987-654-3210', '555-555-5555', '111-222-3333', '444-555-6666']
zipped_data = zip(names, ages, phone_numbers)
result = list(zipped_data)
print(result)
