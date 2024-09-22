from exercise_3 import BankAccount

class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount

jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())