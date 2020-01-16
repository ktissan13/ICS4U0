# J3 Hidden Palindrome 2016
# Tissan Kugathas
# ICS4U0
# September 10 2019

# Ask the user for the word
word = input("Enter the word: ")

# This bool makes is so that the code will stop when it found the longest palindrome
foundpalindrome = True
# This bool allows the code to loop until it finds the longest palindrome
keeplooping = True

# start with the longest possible, work in
for i in range(len(word), 1, -1):
    # loop through every combination with this many letters
    # if it found the palindrome already, then it will break the loop
    if not keeplooping:
        # breaks the loop
        break
    for comb in range(len(word)-i+1):
        if not keeplooping:
            break
        # print('i',i,'comb',comb)#used for testing
        # check if this combination is a palindrome
        foundpalindrome = True  # reset
        for pal_check in range(i//2):
            # print('palcheck',comb+pal_check,'other',comb+i-1-pal_check)#for testing
            # check if letters don't match
            if word[comb+pal_check] != word[comb+i-1-pal_check]:
                foundpalindrome = False
        # if the code found the palindrome it will start to print the output and break the code from further processing
        if foundpalindrome:
            # prints the number of characters that are part of the palindrome
            print('palindrome: ', i)
            # stops the code from procceding further more
            keeplooping = False
            # breaks the loop
            break
# If there is no palindrome and the code keeps on looping then inform user that there is no palindrome
if keeplooping:
    print("No palindrome found")
