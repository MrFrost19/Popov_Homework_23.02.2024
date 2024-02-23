import random

class Shape():
    name = "Shape" # В мене не виходить зробити name = name, але увесть код працює
    colours = ["blue", "red", "green", "yellow"]
    colour = random.choice(colours)


class Circle(Shape):

    name = "Circle"
    def __init__(self):
        self.circle_radius = 3

    def circle_area(self):
        self.area_circle = (self.circle_radius ** 2) * 3.14

    def print_circle(self):
        self.circle_area()
        print(f"{self.name}'s area: {self.area_circle} centietres square "
              f"{self.name}'s colour: {self.colour}")


class Rectangle(Shape):

    name = "Rectangle"
    def __init__(self):
        self.rectangle_lenght = 5
        self.rectangle_width = 3

    def rectangle_area(self):
        self.area_rectangle = self.rectangle_lenght * self.rectangle_width

    def print_rectangle(self):
        self.rectangle_area()
        print(f"{self.name}'s area: {self.area_rectangle} centietres square "
              f"{self.name}'s colour: {self.colour}")


class Triangle(Shape):

    name = "Triangle"
    def __init__(self):
        self.triangle_base = 5
        self.triangle_height = 4

    def triangle_are(self):
        self.area_triangle = (self.triangle_base * self.triangle_height) / 2

    def print_triangle(self):
        self.triangle_are()
        print(f"{self.name}'s area: {self.area_triangle} centietres square "
              f"{self.name}'s colour: {self.colour}")


circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

print(circle.print_circle())
print(rectangle.print_rectangle())
print(triangle.print_triangle())