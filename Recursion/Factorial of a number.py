

def factorial(num):
    if num == 0:
        expo = 1
    else:
        expo = num*factorial(num-1)
    return expo

N = 8000000

print(factorial(N))
