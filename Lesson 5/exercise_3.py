class BankAccount:
    def __init__(self, _name, _balance):
        self.name = _name
        self.balance = _balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств!")
    
    def get_balance(self):
        return self.balance
    
# account = BankAccount("Maria", 1000)
# account.deposit(700)
# account.withdraw(200)
# print(account.get_balance())