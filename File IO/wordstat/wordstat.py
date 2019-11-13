# Word status
# Tissan Kugathas
# ICS4U0
# November 11 2019

order = []

with open('File IO/wordstat/wordstats.txt') as file:
    content = list(file)
    print(content[0])
    line = 1
    nt_line = line + 1
    while len(order) != len(content)-2:
        if line not in order and nt_line not in order:
            if content[line][0] == content[nt_line][0]:
                if ord(content[line][1]) > ord(content[nt_line][1]):
                    highest = line

            else:
                if ord(content[line][0]) > ord(content[nt_line][0]):
                    highest = nt_line
                else:
                    highest = line
        order.append(highest)
        nt_line += 1
    for line in range(1,len(content)):
        if line not in order:
            order.append(line)
    for line in order:
        print(content[line])
