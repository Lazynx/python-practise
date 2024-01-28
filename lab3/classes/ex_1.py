class TwoMethods:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


my_class = TwoMethods()
my_class.get_string()
my_class.print_string()
