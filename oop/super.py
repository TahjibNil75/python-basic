class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.filled = is_filled

    def describe(self):
        print(f"This is a {self.color} shape, and {'filled' if self.filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color,is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with a area of {3.14 * self.radius * self.radius} square units.")

class Square(Shape):
    def __init__(self,color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {0.5 * self.width * self.height} square units.")



circle = Circle(color="red", is_filled=True, radius=5)
print(circle.color)

square = Square(color="blue", is_filled=False, width=4)
triangle = Triangle(color="green", is_filled=True, width=3, height=6)

circle.describe()
square.describe()
triangle.describe()
