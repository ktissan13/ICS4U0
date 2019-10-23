# Adder
# Tissan Kugathas
# ICS 4U0
# October 9 2019

import random

class Adder:

    def __init__(self):
        self.a = random.randint(0,20)
        self.b = random.randint(0,20)

    def getAnswer(self):
        return self.a + self.b

    def start(self):
        user_answer = int(input('{} + {}').format(self.a,self.b))
        

    def __repr__(self):
        return ('A = {} and B = {}').format(self.a,self.b)


class Player:

    def __init__(self):
        self.score = 0

    def addPoints(self,points):
        self.score += points

    def getPoints(self):
        return ('Your score is: {}').format(self.score)

    def __repr__(self):
        return ('Your score is: {}').format(self.score)

player = Player()

loop = True

while loop:

    newgame = Adder()    

    
