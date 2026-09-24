class Car(object):
    year = None
    make = ""
    model = ""

    def __init__(self, year, make="Toyota", model=""):
        self.year = year
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"


car_1 = Car(2022, model="Camry")
car_2 = Car(2023, "Honda", "Civic")

print(car_1.display_info())
print(car_2.display_info())
