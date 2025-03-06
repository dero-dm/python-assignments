class Rectangle:
    # Initialize the rectangle with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
rect = Rectangle(56, 3)  # Create a rectangle with length 5 and width 3
print("Area:", rect.area())  # Output: 15
print("Perimeter:", rect.perimeter())  # Output: 16

