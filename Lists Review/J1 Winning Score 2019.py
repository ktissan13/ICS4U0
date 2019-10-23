# J1 2019 Winning Score
# Tissan Kugathas
# ICS4U0
# September 6 2019

Apples_3point = int(input('Enter the number of three point shoots Apples made: '))
Apples_2point = int(input('Enter the number of two point shoots Apples made: '))
Apples_1point = int(input('Enter the number of one point shoots Apples made: '))

Bananas_3point = int(input('Enter the number of three point shoots Bananas made: '))
Bananas_2point = int(input('Enter the number of two point shoots Bananas made: '))
Bananas_1point = int(input('Enter the number of one point shoots Bananas made: '))


Apples_Totalpoints = Apples_3point * 3 + Apples_2point * 2 + Apples_1point

Bananas_Totalpoints = Bananas_3point * 3 + Bananas_2point * 2 + Bananas_1point

if Apples_Totalpoints > Bananas_Totalpoints:
    print('Apples win')
elif Apples_Totalpoints < Bananas_Totalpoints:
    print('Bananas win')
else:
    print('It is a tie')
