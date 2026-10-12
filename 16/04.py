class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self._age = age

    def __setattr__(self, key, value):
        if key == "_age":
            if not isinstance(value, int) or value < 0 or value > 150:
                print("Age must be a positive integer between 0 and 150.")
        super().__setattr__(key, value)


person = Person("John", "Doe", 100)
print(f"{person.first_name} {person.second_name} is {person._age} years old.")
print("END")

