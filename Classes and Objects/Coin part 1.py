# Coin
# Tissan Kugathas
# ICS4U0
# September 24 2019

import random

class Coin:

    def __init__(self):
        self.face = random.randint(0,1)

    def flipCoin(self):
        self.face = random.randint(0,1)

    def showCoin(self):
        if self.face == 0:
            print('Heads up')
        else:
            print('Tails up')

    def __repr__(self):
        if self.face == 0:
            print('Heads up')
        else:
            print('Tails up')


nickel = Coin()
nickel.flipCoin()
nickel.showCoin()

