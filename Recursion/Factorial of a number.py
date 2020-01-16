# Tissan Kugathas
# Recursion Trial
# ICS4U0
# December 2019


def factorial(num):
    if num == 0:
        expo = 1
    else:
        expo = num*factorial(num-1)
    return expo


N = int(input())
print(factorial(N))
