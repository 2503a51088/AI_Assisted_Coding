class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Generated with an AI coding assistant
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")


# Test with two different inputs
account = BankAccount("BA1001", "Student", 1000)

account.deposit(500)   # Test input 1: balance becomes 1500
account.withdraw(200)  # Test input 2: balance becomes 1300

print("Final balance:", account.balance)