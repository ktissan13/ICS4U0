# J3 Cold Compress 2019
# Tissan Kugathas
# ICS4U0
# September 9 2019

# this input holds all the user inputs
inputs = []
# this ask the user the number lines 
lines = int(input('Enter the number of lines: '))


# this for loop will loop until the number lines the user gave
for current_input in range(lines):
    # this asks the user for the messages and then puts them in a list
    inputs.append(input())

# this loop goes through all the inputs that the user gave
for current_input in inputs:
    # this variable is a string to keep track of the last character
    last_character = ''
    # this variable is a empty string to make the final string
    final_string = ''
    # this variable is the character counter and intiallizes to 0
    count = 0
    for index in range(len(current_input)):
        # this if statement checks if the current index is the last character of the string
        if not index+1 >= len(current_input):
            # this if statement checks if the current character is the same as the next character
            if current_input[index] == current_input[index+1]:
                # this allows the current character to be set as the new last character
                last_character = current_input[index]
                # this increase the character count by 1
                count += 1
            # this else statement is used when the next character is not the same as the current character
            else:
                # this allows the current character to be set as the new last character
                last_character = current_input[index]
                # this increase the character count by 1
                count += 1
                # this creates the string for the current character for the final string
                final_string = final_string + str(count) + ' ' + last_character + ' '
                # this resets the counter to 0
                count = 0
        else:
            # this increase the character count by 1
            count += 1
            # this creates the string for the current character for the final string
            final_string = final_string + str(count) + ' ' + last_character + ' '
            # this resets the counter to 0
            count = 0
# once its done checking the current input, it prints the final string with output of the current input
print(final_string)
            
