from turtle import circle


class Shape:
    def show_shape(self):
        print("Show the shape of figure")
        return "show the shape of figure"

    def unique_shape(self):
        print("This has unique shape")


class Rectangle(Shape):
    def show_shape(self):
        print("shape of the Reactangle is like Lenght and width")


class Circle(Rectangle):
    def show_shape(self):
        print("Show the shape of circle")


class ShapeArea(Circle, Rectangle):
    def __init__(self, height, width, radius):
        self.height = height
        self.width = width
        self.radius = radius

    def show_shape(self):
        pass


rectangle = Rectangle()
rectangle.show_shape()

circle = Circle()
circle.unique_shape()
circle.show_shape()

##Example 2 Mehod overriding clear


class Shapes:
    def show_shape(self):
        return "Return the shape of figure"

    def area(self):
        return "This will give you area of the shape"

    def incorrect_input(self):
        return "Incorrect inputs"


class ReactangleArea(Shapes):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return f"Area of reactangle is {self.height*self.width}"


class Circles(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The area of the circle is {3.14*self.radius**2}"


c = Circles(5)
print(c.area())
print(c.incorrect_input())
r = ReactangleArea(3, 4)
area_of_reactangle = r.area()
print(area_of_reactangle)
