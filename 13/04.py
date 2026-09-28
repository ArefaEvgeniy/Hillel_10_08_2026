class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def func_1(self):
        print(f"This is a {self.make} {self.model}.")

    @staticmethod
    def func_2(years):
        print(f"Kilometers: {years * 1000}")


Car.func_2(3)
car_1 = Car("Toyota", "Camry")
car_1.func_1()
car_1.func_2(5)
