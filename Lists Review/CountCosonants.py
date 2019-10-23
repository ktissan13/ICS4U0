# CountConsonants
# Tissan Kugathas
# ICS3U0
# September 5th 2019

letters = []
vowels = ['a','e','i','o','u','A','E','I','O','U']

text = input('Enter text: ')

for character in text:
    letters.append(character)

consonants = 0

for letter in letters:
    if not letter == ' ':
        if letter not in vowels:
            consonants += 1

print('The number of consonants in', text, 'is', consonants)
        
    
