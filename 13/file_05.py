class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


if __name__ == "__main__":
    point_1 = Point()
    point_2 = Point(3, 4)
    point_3 = Point(6, 8)
    point_4 = Point(3, 4)

    print(f"Point 1: ({point_1.x}, {point_1.y}), Distance from origin: {point_1.distance_from_origin()}")
    print(f"Point 2: ({point_2.x}, {point_2.y}), Distance from origin: {point_2.distance_from_origin()}")

    print(point_3)
    print(point_1)

    print(point_1 == point_3)
    print(point_2 == point_4)
    print("------------------------")
    print(point_1 != point_3)
    print(point_2 != point_4)

    point_5 = point_2 + point_3
    print(point_5)
