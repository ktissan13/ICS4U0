# Coder's Apprentice Excersise 22.1
# Tissan Kugathas
# ICS4U0
# October 28 2019

# This is a class for rectangles
class Rectangle:

    # Initializes rectangle class with x and y coordinates, width and height
    def __init__(self, x, y,w,h):
        # The x coordinates
        self.x = x
        # The y coordinates
        self.y = y
        # The width
        self.w = w
        # The height
        self.h = h

    # Function to get the area of the rectangle
    def area(self):
        # Calculate the area
        return self.w * self.h

    # Function to get the perimeter of the rectangle
    def perminmeter(self):
        # calculate the perimeter
        return 2*(self.w+self.h)

    # The repr function which returns the coordinates, width and height of the rectangle
    def __repr__(self):
        return "[({},{}),w={},h={}]".format(self.x,self.y,self.w,self.h)

# This class is for the square class that inherits the rectangle class
class Square(Rectangle):

    # Initializes square class with x and y coordinates and the length of one side
    def __init__(self,x,y,s):
        # The x coordinates
        self.x = x
        # The y coordinates
        self.y = y
        # The length of one side
        self.s = s
        # Initializes the rectangle class which has been inherited
        super().__init__(x,y,s,s)

    # Function to return the the are of the square
    def square_area(self):
        # Uses the area functions from the super class
        return self.area()

    # Functions to return the perimeter of the square
    def square_perminmeter(self):
        # Uses the perimeter functions from the super class
        return self.perminmeter()

    # The repr function returns the coordinates, length of the side, area, and perimeter of the square
    def __repr__(self):
        return "[({},{}),s={},area={},perminmeter={}]".format(self.x, self.y, self.s,self.square_area(),self.square_perminmeter())

# Sample for the square class
sq = Square(2,1,5)

# Prints the repr function
print(sq)
