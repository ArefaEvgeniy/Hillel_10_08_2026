class MyStr(str):
    def __sub__(self, other):
        if isinstance(other, str):
            return MyStr(self.replace(other, ""))
        return NotImplemented


my_obj_1 = MyStr("Hello, world!")
print(my_obj_1.upper())
print(my_obj_1.strip("H"))
my_obj_2 = MyStr("world")
my_obj_3 = my_obj_1 - my_obj_2
print(my_obj_3)
