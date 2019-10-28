# UEmployee,Faculty,Staff
# Tissan Kugathas
# ICS4U0
# October 28 2019

class UEmployee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def __repr__(self):
        return "The name of the employee is {} and the salary of the employee is {}".format(self.name,self.salary)

class Faculty(UEmployee):

    def __init__(self,name):
        self.name = name
        self.listname  =  []

    def addMembers(self,num):
        for index in range(num):
            self.listname.append(super().__init__(input("Enter the name of the employee"),input("Enter the salary of the employee")))

    def getMembers(self):
        return self.listname

    def getDepartment(self):
        return self.names

    def __repr__(self):
        return "There are {} memebers in the {} department".format(len(self.listname),self.getDepartment())

class Staff(UEmployee):

    def __init__(self,name):
        self.name = name
        self.listname = []

    def addStaff(self,num):
        for index in range(num):
            self.listname.append(super().__init__(input("Enter the name of the staff: "),input("Enter the salary of the staff: ")))

    def getMembers(self):
        return self.name

    def getJobtitle(self):
        return self.name

    def __repr__(self):
        return "There are {} staff who are {}".format(len(self.listname),self.getJobtitle())
