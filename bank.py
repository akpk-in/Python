class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Store the owner's name
        self.balance = balance      # Store the account balance
    
    def deposit(self, amount):
        self.balance += amount      # Add to THIS account's balance
        print(f"{self.owner} deposited ${amount}")
        print(f"New balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Subtract from THIS account's balance
            print(f"{self.owner} withdrew ₹{amount}")
        else:
            print("Insufficient funds!")
    
    def check_balance(self):
        print(f"{self.owner}'s balance: ₹{self.balance}")


# Create bank accounts with names and balances
account1 = BankAccount("Shimjith", 25000000000000000)
account2 = BankAccount("Ajith", 2000000000000000)
account3 = BankAccount("Devika", 1000000000000000)

# Check their balances
account1.check_balance()  # Shimjith's balance: ₹25000000000000000
account2.check_balance()  # Ajith's balance: ₹2000000000000000
account3.check_balance()  # Devika's balance: ₹1000000000000000