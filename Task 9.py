class Rectangle:
    def __init__(self, length, widh) -> None:
        self.length = length
        self.widh = widh
    def area(self):
        return self.length*self.widh
rect1 = Rectangle(43,20)
print(rect1.area())