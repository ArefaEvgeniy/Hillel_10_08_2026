class Woman:
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_age(self):
        res = self._age
        if self._age > 25:
            res = round(self._age * 0.9)
        return res

    def get_weight(self):
        res = self.__weight
        if self.__weight > 50:
            res = round(self.__weight * 0.9)
        elif self.__weight < 40:
            res = round(self.__weight * 1.1)

        return res


woman_1 = Woman("Alice", 30, 60)
print(woman_1.name)  # Output: Alice
print(woman_1._age)  # Output: 30
print(woman_1.get_age())  # Output: 27
print(woman_1._Woman__weight)  # Output: 60
print(woman_1.get_weight())  # Output: 54
