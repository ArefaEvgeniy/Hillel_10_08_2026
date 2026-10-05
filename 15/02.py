from dataclasses import dataclass


@dataclass
class Bell:
    name: str
    weight: float
    material: str
    price: float
    count: int = 0
    total_price: float = 0.0

    def ring(self):
        return f"{self.name} is ringing!"


obj_1 = Bell("Church Bell", 150.0, "Bronze", 5000.0, count=1, total_price=5000.0)
obj_2 = Bell("School Bell", 50.0, "Steel", 1500.0, count=2, total_price=3000.0)
obj_3 = Bell("Door Bell", 5.0, "Plastic", 20.0, count=5, total_price=100.0)

print(obj_1)
print(obj_2.__annotations__)
print(obj_2.__doc__)
print(obj_1.name)
print(obj_1.price)
print(obj_1.total_price)
print(obj_1.ring())
