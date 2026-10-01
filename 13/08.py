class Dog:
    def say(self):
        print("Woof!")

    def go(self):
        print("Dog is running...")

    def bark(self):
        print("Woof! Woof!")


class Dolphin:
    def say(self):
        print("Click!")

    def go(self):
        print("Dolphin is swimming...")

    def swim(self):
        print("Dolphin is swimming fast!")


class Monster(Dolphin, Dog):
    pass


my_obj = Monster()
my_obj.say()
my_obj.go()
my_obj.bark()
my_obj.swim()
