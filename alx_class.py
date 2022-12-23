class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return "car started"

    def stop(self):
        print("car stopped")

    def move(self):
        print("car is moving")


mercedes_e350 = Car("mercedes", "e350")
mercedes_c230 = Car("mercedes", "c230")
# print(f"This is a {mercedes_e350.make} of model {mercedes_e350.model}")
# print(f"This is a {mercedes_c230.make} of model {mercedes_c230.model}")

start_car = mercedes_e350.start()
print(start_car)


class Human:
    def __init__(self, name=str, age=int, race=str, eye_color=str, quirk=str):
        self.name = name
        self.age = age
        self.race = race
        self.eye_color = eye_color
        self.quirk = quirk

    def talk(self):
        print(f"{self.name} is talking to you")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def birthday(self):
        print(f"Hurray!!! It's {self.name}'s {self.age + 1}'th birthday.")


# sam = Human("Sam", 27, "Black", "Brown", "Talks to himself")
# sam.talk()
# sam.birthday()
#
# jules = Human("Jules", 23, "African", "Brown", "Doesn't remember the names of movies she has seen ")
# print(jules.quirk)

def me(f):
    def f():
        return "hi"

    return f


def you():
    pass

print(me)
print(me(you)())



