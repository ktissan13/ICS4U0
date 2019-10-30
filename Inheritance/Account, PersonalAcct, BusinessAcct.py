# Account, PersonalAcct, BusinessAcct Excersise 2
# Tissan Kugathas
# ICS4U0
# October 29 2019

# This a class called Account, it stores the balance of the account and handles the withdraw of the money
class Account:

    # Initializes the balance of the account
    def __init__(self,balance):
        self.balance = balance

    # Returns the balance of the account
    def getBalance(self):
        return self.balance

    # Withdraw the certain amount of money from the account
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount

    # Repr function returns the balance of the account
    def __repr__(self):
        return "The balance in this account is {}".format(self.balance)

# This class is called the PersonalAcct, it inherits the account class but a personal account has different features
class PersonalAcct(Account):

    # Initializes the balance of the account and Initializes the super class
    def __init__(self,p_balance):
        super().__init__(p_balance)

    # This function withdraws the money from the acoount but if the balance is lower than 100 dollars than it will take away 2 dollars
    def PersonalWithdraw(self,amount):
        self.withdraw(amount)
        if self.getBalance() < 100:
            self.withdraw(2)
    # Repr function returns what type of account it is and the amount of money in it
    def __repr__(self):
        return "This is a personal account and it has ${} in it".format(self.getBalance())

# This is class called the BusinessAcct, it inherits the account class but a BusinessAcct has different features tham a personal account
class BusinessAcct(Account):

    # This intiallizes the balance of the account and initializes the super class
    def __init__(self,balance):
        super().__init__(balance)

    # This function withdraws money from the account but if the balance is lower than 500 dollars then it will take away 10 dollars
    def BusinessWithdraw(self,amount):
        self.withdraw(amount)
        if self.getBalance() < 500:
            self.withdraw(10)

    # Repr function returns what type of account it is and the amount of money in it
    def __repr__(self):
        return "This is a business account and it has ${} in it".format(self.balance)

# Sample for the program
Tissan = PersonalAcct(100)

print(Tissan)
Tissan.withdraw(50)
print(Tissan)
