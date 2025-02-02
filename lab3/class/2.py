class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

s = Shape()
b = Square(int(input("Length of the square: ")))
print(s.area(), b.area())


    