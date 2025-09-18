class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f} cm"
    @property
    def height(self):
        return f"{self._height:.2f} cm"
    
    @property
    def areaPrint(self):
        print(f"{self._width * self._height:.2f} cm²")

    @property
    def areaReturn(self):
        return f"{self._width * self._height:.2f} cm²"    
    
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be positive")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be positive")

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

    


rectangle = Rectangle(7, 11)
rectangle.width = 15
rectangle.height = -5
print(rectangle.width)
print(rectangle.height)



    

# rectangle = Rectangle(7, 11)
# print(rectangle.width)
# rectangle.areaPrint
# print(rectangle.areaReturn)


# del rectangle.width
# del rectangle.height