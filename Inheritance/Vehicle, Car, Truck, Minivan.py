# Vehicle, Car, Truck, Minivan
# Tissan Kugathas
# ICS4U0
# October 31 2019


class Vehicle:

    def __init__(self,seats,color,brand):
        self.made = brand
        self.seats = seats
        self.color = color

    def getMade(self):
        return self.made

    def getColor(self):
        return self.color

    def getNumSeats(self):
        return self.seats

    def __repr__(self):
        return "This vehicle is made by {} and it is {} and has {} seats".format(self.made,self.color,self.seats)

class Car(Vehicle):

    def __init__(self,seats,color,brand):
        super().__init__(seats,color,brand)

    def __repr__(self):
        return "This car is made by {} and and it is {} and has {} seats".format(self.made,self.color,self.seats)

class Truck(Vehicle):

    def __init__(self,seats,color,brand):
        super().__init__(seats,color,brand)

    def __repr__(self):
        return "This truck is made by {} and it is {} and has {} seats".format(self.made,self.color,self.seats)

class Minivan(Vehicle):

    def __init__(self,seats,color,brand):
        super().__init__(seats,color,brand)

    def __repr__(self):
        return "This minivan is made by {} and it is {} and has {} seats".format(self.made,self.color,self.seats)

caravan = Minivan(7,'gray','Dodge')
rx7 = Car(2,'yellow','Mazada')
c79 = Truck(2,'white','Volvo')

print(caravan)
print(c79)
print(rx7)
