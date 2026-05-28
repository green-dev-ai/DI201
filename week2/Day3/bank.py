class BankAccount:
    account_number = 1
    def __init__(self, balance=0):
        self.account_number = BankAccount.account_number
        self.balance = balance
        self.transactions = []
        BankAccount.account_number += 1

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)



nate_bank = BankAccount(30_000)
joe_bank = BankAccount(750_000)

print(joe_bank.account_number)
print(nate_bank.account_number)