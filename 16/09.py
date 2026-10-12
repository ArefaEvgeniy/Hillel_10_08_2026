class MyStr(str):

    def __iter__(self):
        self.string = self.split()
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.string):
            result = self.string[self.index].replace(".", "").replace(",", "")
            self.index += 1
            return result.title()
        else:
            raise StopIteration

    def __len__(self):
        return len(self.split())

    def __enter__(self):
        print("Entering the context manager.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context manager.")

    def go(self):
        print("This is a custom method in MyStr class.")


my_str = MyStr("This is a custom string, class AAA.")
print(len(my_str))

with my_str as s:
    for item in s:
        print(item)
    s.go()
    print("end of with block")
print("END")
