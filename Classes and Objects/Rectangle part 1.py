# Rectangle part 1
# Tissan Kugathas
# ICS4U0
# September 24 2019

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def getArea(self):
        return('Area of rectange is:', self.length * self.width)

    def getPerimeter(self):
        return('Perimeter of rectangle is:', self.length*2 + self.width*2)

    def __repr__(self):
        self.getArea()
        self.getPerimeter()

    def __eq__(self,Rectangle):
        return (self.length == Rectangle.length) and (self.width == Rectangle.width)




rect = Rectangle(int(input('Enter Length: ')),int(input('Enter Width: ')))
rect2 = Rectangle(int(input('Enter Length: ')),int(input('Enter Width: ')))

print(rect.getArea())
print(rect.getPerimeter())
print(rect == rect2)

        
        
