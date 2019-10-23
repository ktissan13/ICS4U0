# 2 Nested Objects Assignment
# Tissan Kugathas
# ICS4U0
# October 21 2019

# datetime module to calculate age
from datetime import date

# Course Class 
class Course:

    # Initializes
    def __init__(self,name,num):
        self.course = name
        self.number = num

    # Returns course name
    def getCourse(self):
        return self.course

    # Returns course number
    def getNumber(self):
        return self.number

    # Repr Function which gives course info if called
    def __repr__(self):
        return ('Course name is {} and course number is {}').format(self.course,self.number)

# Student Class which contains info about student
class Student:

    # Initializes
    def __init__(self,first,last,year,month,day,admin,cour,cour2):
        self.first_name = first
        self.last_name = last
        self.birthday = date(year,month,day)
        self.number = admin
        self.course1 = cour
        self.course2 = cour2

    # This function gets the age and returns it 
    def getAge(self):
        # Gets today's date
        today = date.today()
        # Uses todays date and birthday date to determine the age of the student 
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month,self.birthday.day))
        return age

    # This functions get the course name from the Course class and returns it
    def getCourse1Name(self):
        return self.course1.getCourse()

    # This functions get the course number from the course class and returns it
    def getCourse1Num(self):
        return self.course1.getNumber()

    # This functions get the course name from the Course class and returns it
    def getCourse2Name(self):
        return self.course2.getCourse()

    # This functions get the course number from the course class and returns it
    def getCourse2Num(self):
        return self.course2.getNumber()

    # This function returns the students first name
    def getFirstName(self):
        return self.first_name 

    # This function returns the students last name
    def getLastName(self):
        return self.last_name
    
    # This function returns the students adminstration number
    def getAdminNum(self):
        return self.number 

    # Repe Function which returns students info when called
    def __repr__(self):
        return ('Student name is {} {} and is {} years old and is in {}').format(self.first_name,self.last_name,self.getAge(),self.getCourse1Name())
        

# Course that are avaible for students     
Math = Course('Math',101)
English = Course('English',202)
Science = Course('Science',302)
Computer_Science = Course('Computer Science',402)

# This is the list of sample students with all the information needed to initialized the Student class
students = [Student('Tissan','Kugathas',2002,3,13,591142,Computer_Science,Math),Student('Abhinav','Sodhi',2002,12,20,131249,Math,Science),Student('Jackie','Lopez',2001,12,26,784923,English,Science),Student('Parva','Thakkar',2002,6,18,645843,Science,Math)]

# This prints the header for the list/table
print('%-16s%-12s%-12s%-12s%-18s'%('Admin Number:','First Name:','Last Name:','Age:','Courses:')+'\n')

# This prints the info for the list/table for each student in the student list
for student in students:
    print('%-16i%-12s%-12s%-12s%-4s%-17s%-2s%-4s%-18s'%(student.getAdminNum(),student.getFirstName(),student.getLastName(),student.getAge(),student.getCourse1Num(),student.getCourse1Name(),'&',student.getCourse2Num(),student.getCourse2Name()))
    
