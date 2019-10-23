# J2 Time to Decompress 2019
# Tissan Kugathas
# ICS4U0
# September 6 2019

# a function to print a character the number of times the user gives
# it takes to varaible when called called times and string
def repeater (times, string):
    # intiallizes a blank string which be used to display the final product
    final_string = ''
    # this loop run until it runs the certain amount of times the character needs to be printed
    for current in range(times):
        # this adds the character into the blank string variable that we intiallized before
        final_string += string
    # this prints the final string with the number of characters that the user gave
    print(final_string)

# this is a empty list called inputs
# this list will contain all the inputs that the user gave
inputs = []
# this is a variable that allows the user to put a interger value in
# this integer variable will contain the number of lines the message will have
lines = int(input('Enter amount of lines: '))

# this loop is to collect all the inputs from the user
# it runs until it reaches the number of lines the user want the message to have
for current in range(lines):
    print('Enter the number of times you want a character print')
    print('followed by a space input the character you want to print')
    # this ask the user for the number of times the character needs to be printed followed by a space and then the user will input the character
    inputs.append(input())

# this loop will go through all the inputs
for current in inputs:
    # this gets the current input selected and then split into a list
    # this list will make index 0 have the number of times the character needs to printed
    # and index 1 having the character that needs to be printed
    values = current.split()
    # this calls the repeater and uses the values the be spilted from the current user input
    repeater(int(values[0]), values[1])
    
























