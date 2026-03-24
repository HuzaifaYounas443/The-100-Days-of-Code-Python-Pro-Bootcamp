# Step 1: Define Functions
def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial deposit amount: "))
    return {"name": name, "balance": balance}


def deposit(account, amount):
    account['balance'] += amount
    print(f"Deposited {amount}. New balance: {account['balance']}")


def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient balance!")
    else:
        account['balance'] -= amount
        print(f"Withdrew {amount}. New balance: {account['balance']}")


def check_balance(account):
    print(f"Account holder: {account['name']}, Balance: {account['balance']}")


# Step 2: Main Program
def main():
    print("Welcome to the Simple Banking System!")
    account = create_account()

    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            deposit(account, amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(account, amount)
        elif choice == '3':
            return check_balance(account)
        elif choice == '4':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the main program
main()
