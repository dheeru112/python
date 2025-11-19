class BankAccount:
    def __init__(self, name, acc_number):   # FIXED constructor
        self.name = name
        self.acc_number = acc_number
        self.balance = 0.0

    def deposit(self):
        print("\n--- Deposit Money ---")
        try:
            amount = float(input("Enter amount to deposit: ₹ "))
            if amount > 0:
                self.balance += amount
                print(f"Amount ₹{amount} deposited successfully!")
            else:
                print("Invalid amount! Enter a positive value.")
        except ValueError:
            print("❌ Enter numbers only!")

    def withdraw(self):
        print("\n--- Withdraw Money ---")
        try:
            amount = float(input("Enter amount to withdraw: ₹ "))
            if amount <= 0:
                print("Invalid amount! Enter a positive value.")
            elif amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print(f"Amount ₹{amount} withdrawn successfully!")
        except ValueError:
            print("❌ Enter numbers only!")

    def check_balance(self):
        print("\n--- Account Balance ---")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.acc_number}")
        print(f"Current Balance: ₹{self.balance}")


def get_valid_account_number():
    while True:
        acc = input("Enter your bank account number (integer only): ")
        if acc.isdigit():
            print("Account created Successfully!\n") 
            return int(acc)
        else:
            print("❌ Invalid account number! Only integers allowed.")


def main():
    print("===== Welcome to Python Bank Management System =====")
    
    name = input("Enter your name: ")
    acc_number = get_valid_account_number()

    account = BankAccount(name, acc_number)

    while True:
        print("\n===== Menu =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            account.deposit()
        elif choice == '2':
            account.withdraw()
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using our bank system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


main()
