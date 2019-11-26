# BIG BANG THEORY
# Tissan Kugathas
# ICS4U0
# November 25 2019

# user inputs
k = int(input('Enter the K value: '))
string = input('Enter the string: ')

# checks if the inputs are valid
if k < 10 and len(string) <= 20:
    # opens the temp.tmp file to contain the final output
    with open('File IO/temp.tmp','r+') as final:
        # goes through all the characters of string
        for index in range(len(string)):
            # calculates the s value
            s = 3*(index+1) + k
            # if it goes beyond A then it will go back to Z
            if ord(string[index]) - s < ord('A'):
                # calculates the remaining s value
                s = (s - (ord(string[index])-ord('A')))-1
                # gets the decoded letter
                final.write(chr(ord('Z')-s))
            else:
                # gets the decoded letter
                final.write(chr(ord(string[index])-s))
        # prints the final output
        print(final.read())
        # closes file
        final.close()
