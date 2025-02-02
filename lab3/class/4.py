class Point():
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
    def show(self):
        print(self.x, self.y)
    def move(self, x2, y2):
        self.x = x2
        self.y = y2
    def dist(self, second):
        import math
        return math.sqrt((self.x - second.x)**2 + (self.y - second.y)**2)
    
x1, y1 = map(int, input("Enter x1, y1: ").split())
x2, y2 = map(int, input("Enter x2, y2: ").split())
a = Point(x1, y1)
b = Point(x2, y2)
a.show()
b.show()
print(a.dist(b))