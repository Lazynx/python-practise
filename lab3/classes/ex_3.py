class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x - coordinate: {self.x}, y - coordinate: {self.y}")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self):
        print(self.x - self.y)


my_point = Point(5, 10)
my_point.show()
my_point.move(new_x=6, new_y=12)
my_point.show()
my_point.dist()
