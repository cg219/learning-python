class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self.balance}")

    def deposit(self,value):
        self.balance += value
        print("Deposit Accepted")

    def withdraw(self, value):
        if self.balance < value:
            return print("Funds Unavailable!")

        self.balance - value
        print("Withdrawl Accepted")

acct1 = Account('Jose',100)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
