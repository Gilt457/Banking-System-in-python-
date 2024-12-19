import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                      )''')

    # Create Accounts table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Accounts (
                        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        account_type TEXT NOT NULL,
                        balance REAL NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES Users (user_id)
                      )''')

    # Create Transactions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Transactions (
                        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        account_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        transaction_type TEXT NOT NULL,
                        date TEXT NOT NULL,
                        FOREIGN KEY (account_id) REFERENCES Accounts (account_id)
                      )''')

    # Create SavingsGoals table
    cursor.execute('''CREATE TABLE IF NOT EXISTS SavingsGoals (
                        goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        goal_name TEXT NOT NULL,
                        target_amount REAL NOT NULL,
                        current_amount REAL NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES Users (user_id)
                      )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")
