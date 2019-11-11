# Word status
# Tissan Kugathas
# ICS4U0
# November 11 2019

order = []

with open('File IO/wordstats.txt') as file:
    content = list(file)
    print(content[0])
    for line in range(1, len(content)):
        for nt_line in range(1, len(content)):
            if not line == nt_line:
                if content[line][0] == content[nt_line][0]:
                    if ord(content[line][1]) > ord(content[nt_line][1]):
                        highest = line

                else:
                    if ord(content[line][0]) > ord(content[line][0]):
                        highest = line
                    else:
                        highest = nt_line
                order.append(highest)

print(order)
