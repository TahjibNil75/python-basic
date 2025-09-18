from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings


shapes = [Circle(5), Square(5), Triangle(3, 9), Pizza(7, ["cheese", "pepperoni"])]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")