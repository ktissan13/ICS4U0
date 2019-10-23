# J3 Hidden Palindrome 2016 2.0
# Tissan Kugathas
# ICS4U0
# September 9 2019

# Ask user to input the text
string = input("Enter the text: ")
# this takes the text makes sure it is lower cased
string = string.lower()
count = 0

for index1 in range(len(string)):
    string_list = []
    for index2 in (index1, len(string), 1):
        string_list.append(string[index2])
        print(string_list)
##        for index3 in range(len(string)-1, 0, -1):
##            if string[index1] == string[index3]:
##                if index1+1 > count:
##                    count = index1
##                print(count)
##                break
