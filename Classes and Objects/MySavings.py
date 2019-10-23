# My Savings
# Tissan Kugathas
# ICS4U0
# September 25 2019


class PiggyBank():

    def __init__(self,initial):
        self.account = initial

    def addPenny(self):
        self.account += 0.01

    def addNickel(self):
        self.account += 0.05

    def addDime(self):
        self.account += 0.10

    def addQuarter(self):
        self.account += 0.25

    def takeOut(self, amount):
        if self.account > amount:
            self.account -= amount
            num_pennys = (amount//0.01)+1
            num_nickels = (amount//0.05)+1
            num_dimes = (amount//0.10)+1
            num_quarters = amount//0.25
            print('1.Number of Pennys:',int(num_pennys))
            print('2.Number of Nickels:',int(num_nickels))
            print('3.Number of Dimes:',int(num_dimes))
            print('4.Number of Quarters:',int(num_quarters))
            method = int(input('How do you want it: '))
        else:
            print('Insufficient Funds')

    def show(self):
        return "%0.2f" % self.account

    def __repr__(self):
        return ('The Amount: {}').format(self.show())


bank = PiggyBank(float(input("Enter inital amount: ")))
print()
print('1. Show total in bank')
print('2. Add a penny')
print('3. Add a nickel')
print('4. Add a dime')
print('5. Add a quarter')
print('6. Take money out of bank')
print('Enter 0 to quit')
print()

loop = True

while loop:
    selection = int(input("What you gonna do?: "))

    if selection == 0:
        loop = False
    elif selection == 1:
        print(bank)
    elif selection == 2:
        bank.addPenny()
    elif selection == 3:
        bank.addNickel()
    elif selection == 4:
        bank.addDime()
    elif selection == 5:
        bank.addQuarter()
    elif selection == 6:
        bank.takeOut(float(input('Enter the amount you want to take out: ')))

        
        

        
