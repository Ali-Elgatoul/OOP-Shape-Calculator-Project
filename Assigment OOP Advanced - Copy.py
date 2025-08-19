from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def print_shape_details(shape):
    print(f"Area: {shape.area():.2f} square units")
    print(f"Perimeter: {shape.perimeter():.2f} units")

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Details:")
print_shape_details(circle)

print("\nRectangle Details:")
print_shape_details(rectangle)