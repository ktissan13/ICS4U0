# Student marks
# Tissan Kugathas
# ICS4U0
# November 26 2019

import statistics

numofstudents = int(input('Enter the number of students: '))
students = dict()

for student in range(numofstudents):
    name = input('Enter the student name: ')
    mark = int(input('Enter the mark of {}: '.format(name)))
    students[name] = mark

highest = max(students.values())
lowest = min(students.values())
median = statistics.median(students.values())

print(highest,lowest,median)
for student,mark in students.items():
    if mark == highest:
        print(student,'has the highest mark!')
