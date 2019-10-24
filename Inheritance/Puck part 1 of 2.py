# Puck Part 1 of 2
# Tissan Kugathas
# ICS4U0
# October 24 2019

class Puck:

    def __init__(self,weigh,stand,yout):
        self.weigth = weigh
        if 5 <= weigh <= 5.5:
            self.standard = True
        else:
            self.standard = False
        if 4 <= yout <= 4.5:
            self.youth = True
        else:
            self.youth = False
