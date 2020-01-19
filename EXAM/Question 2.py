# Question 2 part 1
# Tissan Kugathas
# ICS4U0
# Janurary 17 2020

# inputs list to keep track of the weight of the carts
inputs = []
valid = []

# compiles the file used to get the input
input_file = open('input.dat', 'r')
temp = list(input_file)
for line in temp:
    inputs.append(line.replace('\n', ''))
# sets the w as the max weigtt of the bridge and n as the number of carts

# for i in range(2):
    # inputs.append(input())

w = int(inputs[0])
n = int(inputs[1])

# for i in range(n):
# inputs.append(input())


# checks if the varaibles are valid
if 1 <= w <= 100000:
    if 1 <= n <= 100000:
        # bool for while loop
        status = True
        # last cart will be 2 since 0 and 1 were the w and n
        last_cart = 2
        # while loop to go through all the carts and to see if they can go through the bridge
        while status:
            current_weight = 0
            for cart in range(last_cart, last_cart+5):
                if cart <= n and int(inputs[cart]) <= w:
                    current_weight += int(inputs[cart])
                if int(inputs[cart]) > w:
                    status = False
                    break

            if current_weight > 100:
                status = False
            elif last_cart-2 >= n:
                status = False
            else:
                for cart in range(last_cart, last_cart+5):
                    print(cart)
                    if cart not in valid:
                        valid.append(cart)

            last_cart += 1
# print the number of carts that can go through
print(len(valid))
