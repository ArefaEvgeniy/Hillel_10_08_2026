class MyIter:
    def __init__(self, start_number):
        self.start_number = start_number

    def __next__(self):
        self.start_number = round((self.start_number + 1) ** 2 / 2)
        return self.start_number


iter_1 = MyIter(2)
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
print(next(iter_1))
