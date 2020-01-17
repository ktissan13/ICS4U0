# Tissan Kugathas
# ICS4U0
# question 1

# recursive function


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


# ask user to input c value
x = int(input('Enter the x value: '))
# ask user to input y value
y = int(input('Enter the y value: '))

# if the input values set
if x >= y and y > 0:
    print(gcd(x, y))
# if not tells user what to input
else:
    print('The x value has to be greater than or equal to the y value and the y value has to be greater than 0')
