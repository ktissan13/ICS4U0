# J3 Hidden Palindrome 2016
# Tissan Kugathas
# ICS4U0
# September 9 2019
    
# Ask user to input the text
string = input("Enter the text: ")
# this takes the text makes sure it is lower cased
string = string.lower()
# this allows the loop to run until it finds the longest loop possible
loop = True
found = False

# this loop goes backwards starting from the index of the last character
for i in range(len(string), 1, -1):
    if not loop:
        break
    # this loop goes forward starting from the index of the first character
    for combination in range(len(string)-i+1):
        if not loop:
            break
        # this loop goes till the half of index 
        for palindrome in range(i//2):
            print(string[combination+palindrome], '|', string[combination+i-1-palindrome])
            if not loop:
                break
            if string[combination+palindrome] == string[combination+i-1-palindrome]:
                found = True
                loop = False
        if found:
            print("Palindrome:", i)
                
