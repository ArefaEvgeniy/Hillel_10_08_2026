my_dict = {
    "age": 20,
    "name": "John",
    "age": 30,
    "city": "New York",
    10: "ten",
    20: "twenty",
    (1, 3, 4): "RRR"
}
print(my_dict)

print(len(my_dict))

print(my_dict["name"])
print(my_dict["city"])
my_dict.update({"age": 31, "country": "USA"})
print(my_dict)
my_dict.update({"children": [{"name": "Alice", "age": 5}, {"name": "Bob", "age": 18}]})
print(my_dict)
print(my_dict[(1, 3, 4)])

print(hash((4, 67, 8)))
print(hash("Hello, world!"))
print(hash("Hello, world!"))
print(hash("Hello, world!"))
print(hash("Hello world!"))

print(my_dict["children"][0]["name"])
if "country" in my_dict:
    print(my_dict["country"])
if "phone" in my_dict:
    print(my_dict["phone"])

print(my_dict.get("country", "Not found"))
print(my_dict.get("phone", "Not found"))
