from datetime import datetime, timedelta


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance
        self.history = []  # Stores transaction history
        self.daily_withdrawals = 0  # Tracks the number of withdrawals per day
        self.last_withdrawal_date = None  # Stores the date of last withdrawal

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance must be positive.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposited ${amount}. Balance: ${self.__balance}"
            self.history.append(transaction)
            print(transaction)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        withdrawal_fee = 5  # Fixed fee per withdrawal
        max_withdrawals_per_day = 3

        today = datetime.now().date()

        # Reset daily withdrawal count if it's a new day
        if self.last_withdrawal_date != today:
            self.daily_withdrawals = 0
            self.last_withdrawal_date = today

        # Check if user has exceeded daily withdrawal limit
        if self.daily_withdrawals >= max_withdrawals_per_day:
            print("Withdrawal limit reached for today.")
            return

        # Check if balance is enough after applying the fee
        if amount + withdrawal_fee > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= (amount + withdrawal_fee)
            self.daily_withdrawals += 1  # Increment daily withdrawal count
            transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrawn ${amount} (Fee: ${withdrawal_fee}). Balance: ${self.__balance}"
            self.history.append(transaction)
            print(transaction)

    def show_history(self):
        print(f"\nTransaction History for {self.account_holder}:")
        for transaction in self.history:
            print(transaction)


# Create multiple users
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Tony", 500)

# Perform transactions
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(100)
account1.withdraw(50)  # Should hit withdrawal limit

account2.deposit(300)
account2.withdraw(600)  # Should fail (Insufficient funds)

# Show transaction history
account1.show_history()
account2.show_history()