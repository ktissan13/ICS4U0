# Puck Part 1 of 2
# Tissan Kugathas
# ICS4U0
# October 24 2019

import math

class Cricle:

    def __init__(self,rad):
        self.radius = rad

    def getRadius(self):
        return self.radius

    def area(self):
        area = round(math.pi*(self.getRadius()**2),2)
        return area

    def __repr__(self):
        return ('The radius of the cricle is {} and the area of the cricle is {}').format(self.radius,self.area())

class Disk(Cricle):

    def __init__(self,t,rad):
        self.thickness = t
        super().__init__(rad)

    def setThickness(self,t):
        self.thickness = t

    def getThickness(self):
        return self.thickness

    def getVolume(self):
        volume = round(self.area()*self.getThickness(),2)
        return volume

    def getSurfaceArea(self):
        surfacearea = round(2*self.area()+2*math.pi*self.getRadius()*self.getThickness(),2)
        return surfacearea

    def __repr__(self):
        return ("The thickness of the disk is {} and the volume is {} and the surface area is {}".format(self.getThickness(),self.getVolume(),self.getSurfaceArea()))

class Puck(Disk):

    def __init__(self,weigh):
        self.standardthick = 1
        self.standardDiameter = 3
        super().__init__(self.standardthick,self.standardDiameter/2)
        self.weight = weigh
        if 5 <= self.weight <= 5.5:
            self.standard = True
        else:
            self.standard = False
        if 4 <= self.weight <= 4.5:
            self.youth = True
        else:
            self.youth = False

    def getWeight(self):
        return self.weight

    def getDivision(self):
        if self.youth and not self.standard:
            return "This puck is for youth"
        elif self.standard and not self.youth:
            return "This puck is standard"
        else:
            return "This puck is not legal for youth nor standard"

    def __repr__(self):
        return ("The puck thickness is {} and the radius is {} and the weight is {}. {}").format(self.getThickness(),self.getRadius(),self.getWeight(),self.getDivision())


youthpuck = Puck(4.2)

print(youthpuck)
