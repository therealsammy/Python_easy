class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Woof!")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


poodle = Dog()
poodle.walk()
poodle.bark()
