# Account, PersonalAcct, BusinessAcct Excersise 2
# Tissan Kugathas
# ICS4U0
# October 29 2019

class Account:

    def __init__(self,balance):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount

    def __repr__(self):
        return "The balance in this account is {}".format(self.balance)


class PersonalAcct(Account):

    def __init__(self,p_balance):
        super().__init__(p_balance)

    def PersonalWithdraw(self,amount):
        self.withdraw(amount)
        if self.getBalance() < 100:
            self.withdraw(2)

    def __repr__(self):
        return "This is a personal account and it has ${} in it".format(self.getBalance())

class BusinessAcct(Account):

    def __init__(self,balance):
        super().__init__(balance)

    def BusinessWithdraw(self,amount):
        self.withdraw(amount)
        if self.getBalance() < 500:
            self.withdraw(10)

    def __repr__(self):
        return "This is a business account and it has ${} in it".format(self.balance)

Tissan = PersonalAcct(100)

print(Tissan)
Tissan.withdraw(50)
print(Tissan)
Tissan.withdraw(20)
print(Tissan)
