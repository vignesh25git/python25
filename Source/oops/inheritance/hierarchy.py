class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping...")

class Car(Vehicle):
    def play_music(self):
        print("Playing music in the car.")

class Bike(Vehicle):
    def do_wheelie(self):
        print("Bike is doing a wheelie!")

class Truck(Vehicle):
    def load_cargo(self):
        print("Loading cargo into the truck.")

c = Car()
b = Bike()
t = Truck()

c.start()
c.play_music()