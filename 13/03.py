from abc import ABC, abstractmethod


class Animal(ABC):
    def born(self):
        print("Animal is born!")

    def die(self):
        print("Animal has died!")

    @abstractmethod
    def say(self):
        pass

    @abstractmethod
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

    def go(self):
        print("Dolphin is swimming...")


dog = Dog()
dolphin = Dolphin()

dog.say()
dolphin.say()
dog.go()
dolphin.go()
