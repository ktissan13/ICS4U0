# Cricle Part 1 or 4
# Tissan Kugathas
# ICS 4U0
# September 23 2019

from math import pi

class Circle:

    def __init__(self, rad):
        self.radius = rad

    def getRadius(self):
        return self.radius

    def circumference(self):
        self.circumference = 2*pi*self.radius
        return self.circumference

    def __repr__(self):
        return ("Yo")

    def __eq__(self,Circle):
        return (Circle.getRadius() == self.getRadius())


spot = Circle(3)
dot = Circle(1)

print(spot.getRadius())
print(spot.circumference())
print(spot)

print(spot == dot)
