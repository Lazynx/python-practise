class Account:
    owner = ""
    balance = 0

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} was withdrew from your account. Your balance: {self.balance}")
        else:
            print("Sorry, this amount of money can't be withdrew. You don't have enough funds!")


my_acc = Account()

my_acc.deposit(100)
my_acc.withdraw(101)
my_acc.withdraw(99)
