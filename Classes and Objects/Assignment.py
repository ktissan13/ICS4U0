# Assignment Nested Objects
# Tissan Kugathas
# ICS 4U0
# October 15 2019

# This is class called rectangle
class Rectangle:

    # initializes the class
    def __init__(self,point,l,w):
        # sets left corner point
        self.left = point
        # sets the length
        self.length = l
        # sets the width
        self.width = w

    # A function that finds the surface area of the rectangle
    def getSurfaceArea(self):
        return (self.length * self.width)

    # A function that finds the perimeter of the rectangle
    def getPerimeter(self):
        return (self.length*2 + self.width*2)

    # A function the finds the right bottom corner of the rectangle 
    def getBottomRight(self):
        temp = self.left.split(',')
        x = int(temp[0])
        y = int(temp[1])
        string = str(self.length+x)+','+str(self.width-y)
        return string

    # a function that creates a new rectangle/ the second rectangle
    def newRectangle(self,point,l,w):
        global sec_rectangle
        sec_rectangle = Rectangle(point,l,w)
        return(sec_rectangle)

    # A function the gets two rectangle finds the overlapping area
    def getOverlapping(self):
        first_point = rectangle.left.split(',')
        second_point = sec_rectangle.left.split(',')
        # This if state checks if the two triangle are overlapping 
        if (int(second_point[0])+sec_rectangle.length) < int(first_point[0]) or (int(first_point[0])+rectangle.length) < int(second_point[0]) or (int(second_point[1])-sec_rectangle.width) > int(first_point[1]) or (int(first_point[1])-rectangle.width) > int(second_point[1]): 
            return ('Not possible, the rectangles are not overlapping')
        else:
            if int(second_point[1]) > int(first_point[1]):
                if int(second_point[0]) > int(first_point[0]):
                    length = ((int(first_point[0])+rectangle.length) - int(second_point[0]))
                    width = (int(first_point[1]) - (int(second_point[1])-sec_rectangle.width))
                else:
                    length = (int(second_point[0])+sec_rectangle.length) - int(first_point[0])
                    width = (int(first_point[1]) - (int(second_point[1])-sec_rectangle.width))
            elif int(second_point[1]) < int(first_point[1]):
                if int(second_point[0]) < int(first_point[0]):
                    length = (int(second_point[0])+sec_rectangle.length) - int(first_point[0])
                    width = (int(second_point[1]) - (int(first_point[1])-rectangle.width))
                else:
                    length = ((int(first_point[0])+rectangle.length)) - (int(second_point[0]))
                    width = (int(second_point[1]) - (int(first_point[1])-rectangle.width))
            shaded_area = length * width
            return('The overlapping area is', shaded_area)

    # repr function 
    def __repr__(self):
        return ('The Rectangle is {} by {} and the left corner is located {}.').format(self.length,self.width,self.left)

# variable for the while loop
loop = True

# initiallizes first rectangle
rectangle = Rectangle(input('Enter the top left corner points: '),int(input('Enter length: ')),int(input('Enter width: ')))

# Variable to keep track if the second rectangle has been made
second_init = False 


# While loop to run user interface
while loop:

    print()
    print('Enter 0. To quit')
    print('Enter 1. To get surface area of rectangle')
    print('Enter 2. To get perimeter of rectangle')
    print('Enter 3. To get the bottom right corner')
    print('Enter 4. To find the overlapping area of the two rectangles')
    print('Enter 5. To make a second Rectangle Object')
    print()

    # Asks the user what they want to do
    choice = int(input('Enter the choice: '))
    print()

    # Runs accroding to what the user wants to do
    if choice == 0:
        loop = False
        break
    elif choice == 1:
        print('The surface area of the first rectangle is',rectangle.getSurfaceArea())
    elif choice == 2:
        print('The perimeter of the first rectangle is',rectangle.getPerimeter())
    elif choice == 3:
        print('The points for the bottom right corner of the first rectangle is', rectangle.getBottomRight())
    elif choice == 4:
        # Checks if the second triangle is initiallized 
        if second_init:
            print(rectangle.getOverlapping())
        else:
            print('Second Triangle has not made. Enter Choice number 5 to make the second triangle')
    elif choice == 5:
        print(rectangle.newRectangle(input('Enter the top left corner points for new rectangle: '),int(input('Enter length for new rectangle: ')),int(input('Enter width for new rectangle: '))))
        # Set the variable to true to state that the second triangle has been initialized
        second_init = True 
