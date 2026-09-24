class Animal:
    tail = True
    legs = 4

    def say(self):
        print("Animal sound!")

    def go(self):
        print("Object is running...")
        for leg in range(self.legs):
            print(f"Leg {leg + 1} is moving...")


class Dog(Animal):

    def say(self):
        print("Woof!")

    def bark(self):
        print("Bark Bark!")


class Cat(Animal):

    def say(self):
        print("Meow!")

    def climbing_tree(self):
        print("Cat is climbing the tree...")


dog_1 = Dog()
dog_2 = Dog()

print(dog_1.legs)
dog_1.say()
dog_1.go()
dog_2.say()

dog_2.legs = 3
dog_2.name = "Buddy"

print(f"Dog 1 legs: {dog_1.legs}")
print(f"Dog 2 legs: {dog_2.legs}")
print(f"Dog 2 name: {dog_2.name}")

print(f"Dog attr: {Dog.__dict__}")
print(f"Dog 1 attr: {dog_1.__dict__}")
print(f"Dog 2 attr: {dog_2.__dict__}")

cat_1 = Cat()
cat_1.say()
cat_1.climbing_tree()

cat_1.go()
dog_2.go()
