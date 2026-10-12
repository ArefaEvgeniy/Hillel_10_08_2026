class MyIter:

    def __init__(self, string):
        self.string = string.split()
        self.index = 0

    def __next__(self):
        if self.index < len(self.string):
            result = self.string[self.index].replace(".", "").replace(",", "")
            self.index += 1
            return result.title()
        else:
            raise StopIteration


class MyStr(str):

    def __iter__(self):
        return MyIter(self)


my_str = MyStr("This is a custom string, class AAA.")

for item in my_str:
    print(item)
