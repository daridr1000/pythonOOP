class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def getBalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount):
        self.balance=self.balance-amount
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
       super().__init__(title,balance)
       self.interestRate=interestRate
    def interestAmount(self):
        return (self.interestRate*self.balance)/100