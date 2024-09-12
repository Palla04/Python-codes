class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage
rectangle = Rectangle(5, 3)
print("Area of rectangle:", rectangle.compute_area())
