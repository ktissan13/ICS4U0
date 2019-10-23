# Game of 21
# Tissan Kugathas
# ICS4U0
# October 8 2019

import random 

class BlackJack:

    def __init__(self):
        self.points = 0

    def reset(self):
        self.points = 0

    def deal(self):
        card = random.randint(1,13)
        if  card == 1:
            value = int(input('You drew an ace! 1 or 11: '))
        elif 2 <= card <= 10:
            string = ('You drew an {}!').format(card)
            print(string)
            value = card
        elif card == 11:
            print('You drew an jack!')
            value = 10
        elif card == 12:
            print('You drew an queen!')
            value = 10
        elif card == 13:
            print('You drew an king!')
            value = 10
        self.points += value
        if self.points < 21:
            return 1
        elif self.points > 21:
            self.reset()
            return 0
        elif self.points == 21:
            return 2

    def getPoints(self):
        return self.points


player = BlackJack()
cpu = BlackJack()

loop = True

print('Lets play black jack \n')

while loop:

    print('Player turn! \n')

    player.reset()
    loop2 = True

    while loop2:
        status = player.deal()

        if status == 1:
            points = ('You have {} points!').format(player.getPoints())
            print(points)
            choice = int(input('Deal(Enter 1) or Stop(Enter 0): '))
            if choice == 0:
                loop2 = False
                break
        elif status == 2:
            print('You have 21 points!')
            loop2 = False
            break
        elif status == 0:
            print('Bust')
            loop2 = False
            break

    print('Computer turn! \n')

    cpu.reset()
    loop3 = True

    while loop3:
        status = cpu.deal()

        if status == 1:
            points = ('Computer has {} points!').format(cpu.getPoints())
            print(points)
            choice = random.randint(0,1)
            if choice == 0:
                loop2 = False
                break
        elif status == 2:
            print('Computer has have 21 points!')
            loop2 = False
            break
        elif status == 0:
            print('Bust')
            loop2 = False
            break

    if cpu.getPoints() > player.getPoints():
        print('Computer Won!')

    
        
