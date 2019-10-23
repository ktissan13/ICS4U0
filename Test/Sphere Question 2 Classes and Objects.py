# Test Classes and Objects Question 2
# Tissan Kugathas
# ICS4U0
# October 10 2019

# Imports the math
import math 

# This a class called Sphere
class Sphere:
    
    # Initalizes the class
    def __init__(self,r):
        # sets the radius to what the user wants the radius to be
        self.radius = r

    # This fuction finds the volume and returns it
    def getVolume(self):
        volume = (4*math.pi*(self.radius**3))/3
        return ("%0.2f"%volume)
    
    # This function finds the surface area and return it
    def getSurfaceArea(self):
        Area = 4*math.pi*(self.radius**2)
        return ("%0.2f"%Area)

    # This 'repr' function returns both the volume and surface area
    def __repr__(self):
        return ('Sphere has radius of {} and a volume of {} and a surface are of {}').format(self.radius,self.getVolume(),self.getSurfaceArea())

# Runs the loop
loop = True

# While loop runs till user tells it stop
while loop:

    # Asks for radius and if enter -1 then the code will stop
    radius = float(input('Enter radius(-1 to exit): '))
    print()

    if radius == -1:
        loop = False
        break
    else:
        # Initailizes the class
        user_sphere = Sphere(radius)
        print('Enter 1 to get volume of the sphere with the radius of',radius)
        print('Enter 2 to get surface area of the sphere with the radius of',radius)
        print('Enter 3 to get both volume and surface area of the sphere with the radius of',radius)

        # Asks the user what they want to do
        choice = int(input('Enter the choice: '))

        # If the user choice is 1, then it will print the volume
        # If the user choice is 2, then it will print the surface area
        # If the user choice is 3, then it will print both volume and surface area
        # If the user choice is anyelse then it will tell the user its an error
        if choice == 1:
            print('The volume of the sphere is',user_sphere.getVolume())
        elif choice == 2:
            print('The Surface Area of the sphere is',user_sphere.getSurfaceArea())
        elif choice == 3:
            print(user_sphere)
        else:
            print('Error')
        
