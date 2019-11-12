# TestProcessor
# Tissan Kugathas
# ICS4U0
# November 12 2019

name = []
answers = []
correct = []

with open('testprocessor.txt') as file:
    content = list(file)
    answer = content[0]
    for line in range(1,len(content)):
        if line/2 != line//2:
            name.append(content[line].replace('\n',''))
        else:
            answers.append(content[line].replace('\n',''))

    for ans in answers:
        right = 0
        for char in range(len(answer)):
            if ans[char] == answer[char]:
                right += 1
        correct.append(right)

    for mark in correct:
        print((mark/len(answer))*100)
                


