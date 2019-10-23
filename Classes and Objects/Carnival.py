# Carnival
# Tissan Kugathas
# ICS4U0
# October 3 2019

import random

class Gamebooth:

    def __init__(self,price,firstprize,conslationPrize):
        self.cost = price
        self.first = firstprize
        self.cons = conslationPrize

    def start(self):
        success = 0
        for current in range(3):
            toss = random.randint(0,1)
            if toss == 1:
                success += 1
        if success == 3:
            return self.first
        else:
            return self.cons 
            

    def getCost(self):
        return self.cost
    

class Player:

    def __init__(self,money):
        self.prizes = ''
        self.wallet = money

    def play(self,game):
        if game.getCost() > self.wallet:
            return ('Sorry, not enough money to play')
        else:
            self.wallet -= game.getCost()
            newPrize = game.start()
            self.prizes = newPrize + ', ' + self.prizes
            return ('Prize won:',newPrize)

    def showPrizes(self):
        return self.prizes
        


balloonDartToss = Gamebooth(2,'tiger plush','sticker')
ringToss = Gamebooth(2,'bear keychain','pencil')
breakAPlate = Gamebooth(1.5,'pig plush','plastic dinosaur')

Shonda = Player(5)
Luis = Player(3)

print('Shonda goes to Ballon Dart Toss.',Shonda.play(balloonDartToss))
print('Luis goes to Ring Toss.',Luis.play(ringToss))
print('Shonda goes to Ring Toss.',Shonda.play(ringToss))
print('Luis goes to Break A Plate.',Luis.play(breakAPlate))
print('Shonda won:',Shonda.showPrizes())
print('Luis won:',Luis.showPrizes())


    
        
    
