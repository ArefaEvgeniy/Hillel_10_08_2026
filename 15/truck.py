from auto import Auto


class Truck(Auto):
    counter = 0

    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        super().display_info()
        print(f"Payload Capacity: {self.payload_capacity} lbs")


if __name__ == "__main__":
    truck_1 = Truck("Ford", "F-150", 2022, 3000)
    truck_2 = Truck("Chevrolet", "Silverado", 2023, 3500)
    obj_1 = Auto("Toyota", "Camry", 2020)
    obj_2 = Auto("Honda", "Civic", 2021)
    obj_3 = Auto("Ford", "Mustang", 2022)

    print(truck_1.counter)
    print(Truck.counter)
    print(obj_3.counter)

