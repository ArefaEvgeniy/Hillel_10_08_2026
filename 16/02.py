class Person:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_value):
        if not isinstance(new_value, int) or new_value < 0 or new_value > 150:
            raise ValueError("Age must be a positive integer between 0 and 150.")
        self._age = new_value


man_1 = Person("John", "Doe")
man_1.age = 67

print(f"{man_1.first_name} {man_1.second_name} is {man_1.age} years old.")

