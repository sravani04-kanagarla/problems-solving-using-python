class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def area(self, r):
        # Area of the circle: π * r^2
        area = 3.14 * r ** 2
        print(f"Area of circle: {area}")

class Rectangle(Shape):
    def area(self, length, breadth):
        # Area of the rectangle: length * breadth
        area = length * breadth
        print(f"Area of rectangle: {area}")

# Create instances of Circle and Rectangle
circle = Circle()
rectangle = Rectangle()

# Call the area method with required arguments
circle.area(5)  # example radius for circle
rectangle.area(10, 5)  # example length and breadth for rectangle

