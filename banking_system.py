import json

# Initialize the dictionary to store account information
bank_accounts = {}

# Function to load data from a JSON file
def load_data():
    global bank_accounts
    try:
        with open("bank_data.json", "r") as file:
            bank_accounts = json.load(file)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Data file is corrupted. Starting fresh.")

# Function to save data to a JSON file
def save_data():
    with open("bank_data.json", "w") as file:
        json.dump(bank_accounts, file, indent=4)
    print("Data saved successfully.")

# Function to create an account
def create_account():
    while True:
        account_number = input("Enter a new account number (5 digits): ")
        if not account_number.isdigit() or len(account_number) != 5:
            print("Invalid account number! It must be a 5-digit number.")
            continue
        if account_number in bank_accounts:
            print("Account already exists!")
            return
        break

    name = input("Enter account holder's name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    pin = input("Set a 4-digit PIN for your account: ")
    if not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN! It must be a 4-digit number.")
        return

    bank_accounts[account_number] = {
        "name": name,
        "balance": initial_deposit,
        "pin": pin,
        "transactions": [f"Account created with initial deposit of ${initial_deposit}"],
        "savings_goal": None
    }
    save_data()
    print(f"Account for {name} created successfully!")

# Function to deposit money
def deposit():
    account_number = input("Enter your account number: ")
    if account_number not in bank_accounts:
        print("Account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[account_number]["pin"] != pin:
        print("Incorrect PIN!")
        return

    amount = float(input("Enter amount to deposit: "))
    bank_accounts[account_number]["balance"] += amount
    bank_accounts[account_number]["transactions"].append(f"Deposited ${amount}")
    save_data()
    print(f"${amount} deposited successfully!")

# Function to withdraw money
def withdraw():
    account_number = input("Enter your account number: ")
    if account_number not in bank_accounts:
        print("Account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[account_number]["pin"] != pin:
        print("Incorrect PIN!")
        return

    amount = float(input("Enter amount to withdraw: "))
    if bank_accounts[account_number]["balance"] < amount:
        print("Insufficient balance!")
        return
    bank_accounts[account_number]["balance"] -= amount
    bank_accounts[account_number]["transactions"].append(f"Withdrew ${amount}")
    save_data()
    print(f"${amount} withdrawn successfully!")

# Function to check balance
def check_balance():
    account_number = input("Enter your account number: ")
    if account_number not in bank_accounts:
        print("Account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[account_number]["pin"] != pin:
        print("Incorrect PIN!")
        return

    balance = bank_accounts[account_number]["balance"]
    print(f"Your balance is: ${balance}")

# Function to view transaction history
def view_transactions():
    account_number = input("Enter your account number: ")
    if account_number not in bank_accounts:
        print("Account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[account_number]["pin"] != pin:
        print("Incorrect PIN!")
        return

    transactions = bank_accounts[account_number]["transactions"]
    print("\nTransaction History:")
    for transaction in transactions:
        print(f"- {transaction}")

# Function to apply interest to all accounts
def apply_interest():
    rate = float(input("Enter annual interest rate (as a percentage): "))
    for account_number, details in bank_accounts.items():
        interest = details["balance"] * (rate / 100)
        details["balance"] += interest
        details["transactions"].append(f"Interest of ${interest} applied")
    save_data()
    print(f"Interest applied to all accounts at {rate}% rate.")

# Function to transfer funds between accounts
def transfer_funds():
    from_account = input("Enter your account number: ")
    if from_account not in bank_accounts:
        print("Sender account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[from_account]["pin"] != pin:
        print("Incorrect PIN!")
        return

    to_account = input("Enter recipient account number: ")
    if to_account not in bank_accounts:
        print("Recipient account not found!")
        return

    amount = float(input("Enter amount to transfer: "))
    if bank_accounts[from_account]["balance"] < amount:
        print("Insufficient balance!")
        return

    bank_accounts[from_account]["balance"] -= amount
    bank_accounts[to_account]["balance"] += amount
    bank_accounts[from_account]["transactions"].append(f"Transferred ${amount} to account {to_account}")
    bank_accounts[to_account]["transactions"].append(f"Received ${amount} from account {from_account}")
    save_data()
    print(f"${amount} transferred successfully!")

# Function to delete an account
def delete_account():
    account_number = input("Enter your account number: ")
    if account_number not in bank_accounts:
        print("Account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[account_number]["pin"] != pin:
        print("Incorrect PIN!")
        return

    confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
    if confirm == "yes":
        del bank_accounts[account_number]
        save_data()
        print("Account deleted successfully!")
    else:
        print("Account deletion canceled.")

# Function to set a savings goal
def set_savings_goal():
    account_number = input("Enter your account number: ")
    if account_number not in bank_accounts:
        print("Account not found!")
        return
    pin = input("Enter your 4-digit PIN: ")
    if bank_accounts[account_number]["pin"] != pin:
        print("Incorrect PIN!")
        return

    goal = float(input("Enter your savings goal amount: "))
    bank_accounts[account_number]["savings_goal"] = goal
    save_data()
    print(f"Savings goal of ${goal} set successfully!")

# Main program loop
def main():
    load_data()
    while True:
        print("\nWelcome to the Banking System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Apply Interest")
        print("7. Transfer Funds")
        print("8. Delete Account")
        print("9. Set Savings Goal")
        print("10. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            apply_interest()
        elif choice == "7":
            transfer_funds()
        elif choice == "8":
            delete_account()
        elif choice == "9":
            set_savings_goal()
        elif choice == "10":
            save_data()
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

