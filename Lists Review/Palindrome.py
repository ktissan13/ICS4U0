# Palindrome 
# Tissan Kugathas
# ICS4U0
# September 5th 2019

letters = []

original_message = input("Enter a string: ")

for character in original_message:
    letters.append(character)

letters.reverse()

new_message = ''

for letter in letters:
    new_message = new_message + letter

if original_message == new_message:
    print(original_message,'is a palindrome')
else:
    print(original_message,'is not a palindrome')
