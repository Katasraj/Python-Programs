class BankAccount:
    def __init__(self,Account_Number,IR,Balance=0):
        self.Account_Number = Account_Number
        self.Balance = Balance
        self.IR = IR

    def deposit(self,amount):
        total_amount = self.Balance+amount
        self.Balance = total_amount
        #return f"Aftre depositing {amount}, available balance is {self.Balance}"

    def withdraw(self,withdraw):
        if withdraw > self.Balance:
            print(f"In sufficiant balance try withdraw not more than {self.Balance}")
            return
        total_amount = self.Balance-withdraw
        self.Balance = total_amount
        #return f"Aftre withdrawing {withdraw}, available balance is {self.Balance}"

    def Intrest(self):
        r = round((self.IR/1200)*self.Balance,2)
        self.Balance = self.Balance+r
        #return f"Intrest  is {r} and total balance {self.Balance}"

    def __str__(self):
        return f"Account Information: A/C No {self.Account_Number}, Total Balance {self.Balance} on IntrestRate {self.IR}"


a = BankAccount(123,12.5, 100)
b = a.deposit(100000)
c = a.withdraw(100)
d = a.Intrest()

print(a)


