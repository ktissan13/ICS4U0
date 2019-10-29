# UEmployee,Faculty,Staff
# Tissan Kugathas
# ICS4U0
# October 28 2019

# UEmployee class which has the records of the employee
class UEmployee:


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # Function which returns the name of the employee
    def getName(self):
        return self.name

    # Function which returns the salary of the employee
    def getSalary(self):
        return self.salary

    # Repr function which returns the name of the employee and the salary
    def __repr__(self):
        return "The name of the employee is {} and the salary of the employee is {}".format(self.name,self.salary)

# Faculty class which stores the members and info about the department
class Faculty(UEmployee):

    def __init__(self,name):
        self.name = name
        self.listname  =  []

    # Function that allows the user to enter members to the department
    def addMembers(self,num):
        for index in range(num):
            self.listname.append(super().__init__(input("Enter the name of the employee"),input("Enter the salary of the employee")))

    # Function that returns info about each employee in the department
    def getMembers(self):
        for index in self.listname:
            return index

    # Function that returns the name of the department
    def getDepartment(self):
        return self.names

    # Repr function that returns the name of the department and the number of members
    def __repr__(self):
        return "There are {} memebers in the {} department".format(len(self.listname),self.getDepartment())

# Staff class which stores staff information and the members
class Staff(UEmployee):

    def __init__(self,name):
        self.name = name
        self.listname = []

    # Function that allows the user toenter members of the department
    def addStaff(self,num):
        for index in range(num):
            self.listname.append(super().__init__(input("Enter the name of the staff: "),input("Enter the salary of the staff: ")))

    # Function that returns info about each staff
    def getMembers(self):
        return self.name

    # Function that returns the job title
    def getJobtitle(self):
        return self.name

    # Function that returns the number of staff that have the job title
    def __repr__(self):
        return "There are {} staff who are {}".format(len(self.listname),self.getJobtitle())
