# Word Count
# Tissan Kugathas
# ICS4U0
# November 11 2019

num_lines = 0
num_words = 0

with open("File IO/source.txt", 'r') as file:
    for line in file:
        num_lines += 1
        for word in line:
            num_words += 1

average = num_words / num_lines

print(round(average))
