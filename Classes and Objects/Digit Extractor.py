# Digit Extractor
# Tissan Kugathas
# ICS4U0
# September 26 2019


class DigitExtractor:

    def __init__(self, num):
        self.integer = num

    def showWhole(self):
        print('The whole number is:',self.integer)

    def showOnes(self):
        string = str(self.integer)
        print('The ones place digit is:',string[len(string)-1])

    def showTens(self):
        string = str(self.integer)
        print('The tens place digit is:',string[len(string)-2])

    def showHundreds(self):
        string = str(self.integer)
        print('The hundreds place digit is:',string[len(string)-3])

    def __repr__(self):
        return ('The whole number is: {}').format(self.showWhole())


number = DigitExtractor(int(input('Enter an integer: ')))

loop = True 

while loop:
    print()
    print('Show (W)hole number')
    print('Show (O)nes place number')
    print('Show (T)ens place number')
    print('Show (H)undreds place number')
    print('(Q)uit')
    print()
    user_input = input('Enter your choice: ')
    choice = user_input.upper()
    if choice == 'W':
        number.showWhole()
    elif choice == 'O':
        number.showOnes()
    elif choice == 'T':
        number.showTens()
    elif choice == 'H':
        number.showHundreds()
    elif choice == 'Q':
        loop = False
        
    
