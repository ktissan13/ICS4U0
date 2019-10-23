# Test Classes and Objects Question 1 
# Tissan Kugathas
# ICS4U0
# October 10 2019

# Imports Math Library
import math

# Class called point
class Point:

    def __init__(self,x,y):
        self.grid = []
        for colum in range(4):
            self.grid.append([])
            self.grid[colum].append([])
        self.grid[0] = x
        self.grid[0][1] = y
        

##    def newCoords(self):
##        
##
##    def getList(self):
##        return self.grid
##
##    def __repr__(self):
##        return ('Points of the corner are {}').format(self.getList())
    
        

class Rectangle:

    def __init__(self,l,w):
        self.length = l
        self.width = w

    def newLength(self,length):
        self.length = length

    def newWidth(self):
        self.width = width

    #def getCord(self,rectangle):
        
        

    #def __repr__(self):
        


length = int(input('Enter the length of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
cords = input('Enter the coordinates for left hand corner: ')

initial_coord = cords.split(',')
points = (int(initial_coord[0]),int(initial_coord[1]))
rectangle = Rectangle(length,width)





