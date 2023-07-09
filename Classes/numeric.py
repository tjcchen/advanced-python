#
# give objects number-like behavior
#

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # implement addition, override __add__
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    # implement subtraction, override __sub__
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    # implement in-place addition, override __iadd__
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    # declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)  # <Point x:10,y:20> <Point x:30,y:30>

    # add two points
    # p3 = p1 + p2  # TypeError: unsupported operand type(s) for +: 'Point' and 'Point', if we didn't define __add__
    p3 = p1 + p2
    print(p3)  # <Point x:40,y:50>

    # subtract two points
    p4 = p2 - p1
    print(p4)  # <Point x:20,y:10>

    # perform in-place addition
    p1 += p2
    print(p1)  # <Point x:40,y:50>


if __name__ == "__main__":
    main()
