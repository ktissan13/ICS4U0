# Test Question 2
# Tissan Kugathas
# ICS4U0
# November 25 2019

# opens the file with  input
with open('File IO/Crypto Columns/input.dat') as userinput:
    # makes a list of the contents of the file
    content = list(userinput)
    # goes to through each set of input
    for index in range(0,(len(content)-1),2):
        # gets the keyword
        keyword = content[index]
        # gets the string that needs to be decoded
        coded = content[index+1]
        # keeps the order of index of the character
        order = []
        # finds out the order of letters accsending order
        for index2 in range(len(keyword)):
            if index2 not in order:
                highest = index2
                for index3 in range(len(keyword)):
                    if index3 not in order and index2 != index3:
                        if ord(keyword[highest]) < ord(keyword[index3]):
                            highest = index3
                        if highest not in order:
                            order.append(highest)
                for colum in order:
                    s = (len(coded)//len(keyword))*colum

            
