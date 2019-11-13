# MadLib
# Tissan Kugathas
# ICS4U0
# November 13 2019

from random import randint
semi = []
final = []
story = []

with open('File IO/madlib/story.txt') as stories:
    temp = list(stories)
    for line in temp:
        story.append(line.replace('\n',''))

    with open('File IO/madlib/nouns.txt') as nouns:
        content = list(nouns)
        list_nouns = []
        for line in content:
            list_nouns.append(line.replace('\n',''))
        for line in story:
            semi.append(line.replace('#',list_nouns[randint(0,len(list_nouns)-1)]))

    with open('File IO/madlib/verbs.txt') as verbs:
        content = list(verbs)
        list_verbs = []
        for line in content:
            list_verbs.append(line.replace('\n',''))
        for line in semi:
            final.append(line.replace('%',list_verbs[randint(0,len(list_verbs)-1)]))

    for line in final:
        print(line)
