class Animal:
    def born(self):
        print("Animal is born!")

    def die(self):
        print("Animal has died!")

    def say(self):
        pass

    def go(self):
        pass


class Dog(Animal):
    def say(self):
        print("Woof!")

    def go(self):
        print("Dog is running...")


class Dolphin(Animal):
    def say(self):
        print("Click!")


dog = Dog()
dolphin = Dolphin()

dog.say()
dolphin.say()
dog.go()
dolphin.go()

animal = Animal()
animal.say()
animal.go()
animal.born()
