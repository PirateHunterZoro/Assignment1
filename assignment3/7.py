"""
circle
"""

from math import pi

class circle():
    def __init__(self,r=1):
        self.r=r

    def perimeter(self): return 2*pi*self.r

    def area(self): return pi*(self.r ** 2)


if __name__ == "__main__":
    c = circle(int(input("Enter the radius of the circle")))
    print("Area is {}".format(c.area()))
    print("Perimeter is {}".format(c.perimeter()))
