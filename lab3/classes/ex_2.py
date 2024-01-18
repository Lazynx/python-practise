class Shape:
    def __init__(self):
        self.area = 0

    def print_area(self):
        print(self.area)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.square_length = length


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def find_area(self):
        self.area = self.length * self.width


my_rectangle = Rectangle(2, 3)
my_rectangle.find_area()
my_rectangle.print_area()
