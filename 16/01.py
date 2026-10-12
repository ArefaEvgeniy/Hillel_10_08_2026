class Person:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    @full_name.setter
    def full_name(self, name):
        first, second = name.split(" ")
        self.first_name = first
        self.second_name = second

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.second_name = None
        print("Full name deleted!")


man = Person("John", "Doe")
print(man.first_name)
print(man.second_name)
print(man.full_name)
print("------------------------------")

man.second_name = "Smith"
print(man.first_name)
print(man.second_name)
print(man.full_name)
print("------------------------------")

man.full_name = "Nick Johnson"
print(man.first_name)
print(man.second_name)
print(man.full_name)
print("------------------------------")

del man.full_name
print(man.first_name)
print(man.second_name)


