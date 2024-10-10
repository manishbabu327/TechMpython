import sys 

class Account:
    def __init__(self, accno, name, balance=0):
        self.accno = accno
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"Account created with balance {balance}")
        
    def view_details(self):
        print(f"\nAccount Number: {self.accno}")
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}, Balance: {self.balance}")
            print(f"\nDeposited {amount}. New balance is {self.balance}.")
        else:
            print("\nDeposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}, Balance: {self.balance}")
            print(f"\nWithdrawn {amount}. New balance is {self.balance}.")
        else:
            print("\nInsufficient balance or invalid amount.")
    
    def transfer(self, target_acc, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_acc.balance += amount
            self.transactions.append(f"Transferred {amount} to Account {target_acc.accno}, Balance: {self.balance}")
            target_acc.transactions.append(f"Received {amount} from Account {self.accno}, Balance: {target_acc.balance}")
            print(f"\nTransferred {amount} to Account {target_acc.accno}.")
        else:
            print("\nTransfer failed due to insufficient balance or invalid amount.")
    
    def print_transactions(self):
        print(f"\nTransaction history for account {self.accno}:")
        for transaction in self.transactions:
            print(transaction)

class BankApp:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        accno = input("\nEnter account number: ")
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial deposit: "))
        if accno in self.accounts:
            print("\nAccount with this number already exists.")
        else:
            self.accounts[accno] = Account(accno, name, balance)
            print("\nAccount created successfully.")
    
    def view_account(self):
        accno = input("\nEnter account number: ")
        if accno in self.accounts:
            self.accounts[accno].view_details()
        else:
            print("\nAccount not found.")
    
    def withdraw(self):
        accno = input("\nEnter account number: ")
        if accno in self.accounts:
            amount = float(input("Enter amount to withdraw: "))
            self.accounts[accno].withdraw(amount)
        else:
            print("\nAccount not found.")
    
    def deposit(self):
        accno = input("\nEnter account number: ")
        if accno in self.accounts:
            amount = float(input("Enter amount to deposit: "))
            self.accounts[accno].deposit(amount)
        else:
            print("\nAccount not found.")
    
    def transfer(self):
        accno_from = input("\nEnter your account number: ")
        if accno_from in self.accounts:
            accno_to = input("Enter target account number: ")
            if accno_to in self.accounts:
                amount = float(input("Enter amount to transfer: "))
                self.accounts[accno_from].transfer(self.accounts[accno_to], amount)
            else:
                print("\nTarget account not found.")
        else:
            print("\nYour account not found.")
    
    def print_transactions(self):
        accno = input("\nEnter account number: ")
        if accno in self.accounts:
            self.accounts[accno].print_transactions()
        else:
            print("\nAccount not found.")
    
    def menu(self):
        while True:
            print("\n--- Bank Menu ---")
            print("1. Create Account")
            print("2. View Account Details")
            print("3. Withdraw")
            print("4. Deposit")
            print("5. Transfer Funds")
            print("6. Print Transaction History")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.view_account()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.deposit()
            elif choice == '5':
                self.transfer()
            elif choice == '6':
                self.print_transactions()
            elif choice == '7':
                print("\nExiting... Goodbye!")
                sys.exit()
            else:
                print("\nInvalid choice. Please try again.")

# Create a BankApp instance and display the menu
if __name__ == "__main__":
    app = BankApp()
    app.menu()
