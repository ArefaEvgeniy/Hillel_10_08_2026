class Auto:
    counter = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.increment_counter()

    @classmethod
    def increment_counter(cls):
        cls.counter += 1

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


if __name__ == "__main__":
    obj_1 = Auto("Toyota", "Camry", 2020)
    obj_2 = Auto("Honda", "Civic", 2021)
    print(obj_1.counter)
    obj_3 = Auto("Ford", "Mustang", 2022)
    print(Auto.counter)
    print(obj_1.counter)
