# Course Grade
# Tissan Kugathas
# ICS4U0
# September 11 2019

# A list that will contain the student grades
student = []
# A list that will contain the student names 
student_name = []

# This asks the user how many students are in class
num_students = int(input('Enter the number of students: '))

# This for loop will create the more list inside the student list
for student_num in range(num_students):
    #Add more list into the student list
    student.append([])

# This for loop is to ask the names of each student in the class
# Each student has a student number to keep track of their grades
for student_num in range(len(student)):
    # Ask the user for each students name and then puts in the name list
    student_name.append(input("Enter student {}'s name: " .format(str(student_num+1))))

# This for loop is to get the grades of each student 
for student_num in range(num_students):
    # this a temperory list to hold the grades of the current student
    grades = []
    # This asks the user to enter the grades of the students
    # The grades enter and follwed by a comma if there are any other grades
    user_input = str(input("Enter {}'s grades: " .format(str(student_name[student_num]))))
    # The grades then split with the comma and go into the student list which is the list that will contain the grades
    grades = user_input.split(',')
    # for loop to up all the current students grade into the student list in their student number
    for grade in grades:
        student[student_num].append(int(grade))

# This is a bool so the user for the user interface below        
loop = True

# These codes below are a series function and work when called
# This function gets the name of a student and displays the grades of that student
def studentGrades(name):
    student_num = student_name.index(name)
    print("{}'s grades are" .format(str(student_name[student_num])), student[student_num])

# This function gets the name of a student and displays the average of that student
def studentAvg(name):
    student_num = student_name.index(name)
    grade_sum = 0
    for grade in student[student_num]:
        grade_sum += grade
    avg = grade_sum//len(student[student_num])
    print("{}'s average is" .format(str(student_name[student_num])), str(avg) + '%')

# This function gets the test number of a test and displays the class average of that test
def testAvg(test):
    student_num = student_name.index(name)
    test_sum = 0
    for student_num in range(len(student)):
        test_sum += student[student_num][test]
    avg = test_sum//len(student)
    print('Test {} average is' .format(str(test)), str(avg)+'%')

while loop:
    # These are user rules for the code
    print()
    print('For student grades, enter 1')
    print('For student average, enter 2')
    print('For test average, enter 3')
    print('To stop code, enter 4')
    print()
    # This asks the user what they want to do
    selection = int(input("Enter a selection: "))
    # If the user wants to find out a students grade
    # Then it ask for the student's name and display the grades
    if selection == 1:
        name = input('Enter the student name: ')
        studentGrades(name)
    # If the user wants to find out a students average
    # Then it asks for the students name and display the average of that student
    if selection == 2:
        name = input('Enter the student name: ')
        studentAvg(name)
    # If the user wants to find out the class average of a test
    # Then it asks for the test number of the test the user wants and displays the test average of that test
    if selection == 3:
        test = int(input('Enter the test number: '))
        testAvg(test)
    # If the user wants to stop the code, then the code will stop
    if selection == 4:
        loop = False
    


        
