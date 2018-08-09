# Replace "pass" with your code

class BankAccount(object):
    def __init__(self,label,balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        return "{0} {1}".format(self.label,self.balance)

    def withdraw(self,amount):
        if amount > 0 and (balance - amount) >= 0:
            self.balance -= amount

    def withdraw(self,amount):
        if amount > 0:
            self.balance += amount

    def rename(self,amount):
        if name != "":
            self.label = name

    def transfer(self,dest_account,amount):
        if amount > 0 and (self.balance - amount) >= 0:
            dest_account.deposit(amount)
            self.withdraw(amount)
