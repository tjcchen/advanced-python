#
# namedtuple
#

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20) 
    p2 = Point(30, 40)
    print(p1, p2)     # Point(x=10, y=20) Point(x=30, y=40)
    print(p1.x, p2.y) # 10 40, access tuple by its name

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    p2 = p2._replace(x=11, y=22)
    print(p1)         # Point(x=100, y=20)
    print(p2)         # Point(x=11, y=22)


if __name__ == "__main__":
    main()
