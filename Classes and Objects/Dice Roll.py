# Dice Roll
# Tissan Kugathas
# ICS4U0
# Ocotober 7 2019

import random

class Die:

    def __init__(self):
        self.score = 1000

    def roll(self,risk,call):
        total = random.randint(1,6) + random.randint(1,6)
        print('You rolled:', total)
        if 2 <= total <= 6 and call == 0:
            self.score += risk*2
        if 8 <= total <= 12 and call == 1:
            self.score += risk*2
        else:
            self.score -= risk

    def __repr__(self):
        return ('You have {} points').format(self.score)

loop = True
DRPlayer = Die()

while loop:
    print(DRPlayer)
    risk = int(input('How many points do you want to risk?(-1 to quit): '))
    if risk > -1 and risk != 0:
        call = int(input('Make a call(0 for low, 1 for high): '))
        if 0 <= call <= 1:
            DRPlayer.roll(risk,call)
    elif risk == 0:
        print('The number of points you want to risk has to be greater than 0')
    else:
        loop = False

        
