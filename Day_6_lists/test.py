import random

class Person:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.last = last_name

    def talk(self):
        print(f"Hey there {self.name}")

john = Person("Johhny", "Priednieks")
print(john.name)
john.talk()

