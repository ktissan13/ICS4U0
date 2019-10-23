# Lunch Order
# Tissan Kugathas
# ICS 4U0
# October 7 2019

class food:

    def __init__(self,nom,price,fat,carb,fibe):
        self.name = nom
        self.cost = float(price)
        self.fat = float(fat)
        self.carbs = float(carb)
        self.fiber = float(fibe)

    def getCost(self):
        return self.cost

    def __repr__(self):
        return ('Each {} has {}g of fat {}g of carbs, and {}g of fiber.').format(self.name,self.fat,self.carbs,self.fiber)

hamburger = food('hamburger',1.85,9,33,1)
salad = food('salad',2,1,11,5)
french_fries = food('french fries',1.30,11,36,4)
soda = food('soda',0.95,0,38,0)

num_of_hamburgers = int(input('Enter number of hamburgers: '))
print(hamburger)
num_of_salad = int(input('Enter number of salad: '))
print(salad)
num_of_fries = int(input('Enter number of fries: '))
print(french_fries)
num_of_soda = int(input('Enter number of sodas: '))
print(soda)



total_cost = hamburger.getCost()*num_of_hamburgers + salad.getCost()*num_of_salad + french_fries.getCost()*num_of_fries + soda.getCost()*num_of_soda

print("Your order cost:", total_cost)
