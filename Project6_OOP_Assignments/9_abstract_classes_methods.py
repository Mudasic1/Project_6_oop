from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass
    
    def describe(self):
        """Non-abstract method that all child classes can use."""
        return "This is a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def describe(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):
        return f"Circle with radius {self.radius}"

# Test the abstract class and concrete implementations
if __name__ == "__main__":
    # Cannot instantiate an abstract class
    try:
        shape = Shape()
        print("Created a Shape instance")
    except TypeError as e:
        print(f"Error creating Shape instance: {e}")
    
    # Create a Rectangle instance
    rectangle = Rectangle(5, 10)
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Rectangle Perimeter: {rectangle.perimeter()}")
    print(f"Rectangle Description: {rectangle.describe()}")
    
    # Create a Circle instance
    circle = Circle(7)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")
    print(f"Circle Description: {circle.describe()}") 