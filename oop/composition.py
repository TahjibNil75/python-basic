## Composition = Objects that can not exists independently. "own a " relationship.


class Engine:
    def __init__(self, horsePower):
        self.horsePower = horsePower


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size)for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} with {self.engine.horsePower} HP and {len(self.wheels)} wheels of size {self.wheels[0].size} inches."
    

car1 = Car("Toyota", "Camry", 200, 16) 
car2 = Car("Honda", "Civic", 180, 15)

print(car1.display_car())
print(car2.display_car())
