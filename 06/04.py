my_dict = {"name": "John", "age": 30, "city": "New York", "country": "USA"}

for key in my_dict:
    print(f"{key} - {my_dict[key]}")

print("--------------------")
for item in my_dict.keys():
    print(item)

print("--------------------")
for item in my_dict.values():
    print(item)

print("--------------------")
for item in my_dict.items():
    print(item)

print("--------------------")
for key, value in my_dict.items():
    print(f"{key} - {value}")
