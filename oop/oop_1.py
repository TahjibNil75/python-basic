class Car:
    
    make = None
    model = None
    year = None
    color = None

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        return f"The {self.color} {self.make} {self.model} is driving."
    
    def stop(self):
        return f"The {self.color} {self.make} {self.model} has stopped."
    

car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2019, "Blue")

print(car1.drive())

