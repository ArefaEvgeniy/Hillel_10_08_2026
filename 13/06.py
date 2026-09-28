from file_05 import Point


class Circle(Point):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius


circle_1 = Circle(0, 5, 3)
print(circle_1.x, circle_1.y, circle_1.radius)
print(circle_1)
