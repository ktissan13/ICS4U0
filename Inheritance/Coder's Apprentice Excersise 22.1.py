# Coder's Apprentice Excersise 22.1
# Tissan Kugathas
# ICS4U0
# October 28 2019

class Rectangle:

    def __init__(self, x, y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perminmeter(self):
        return 2*(self.w+self.h)

    def __repr__(self):
        return "[({},{}),w={},h={}]".format(self.x,self.y,self.w,self.h)

class Square(Rectangle):

    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
        super().__init__(x,y,s,s)

    def square_area(self):
        return self.area()

    def square_perminmeter(self):
        return self.perminmeter()

    def __repr__(self):
        return "[({},{}),s={},area={},perminmeter={}]".format(self.x, self.y, self.s,self.square_area(),self.square_perminmeter())

sq = Square(2,1,5)

print(sq)
