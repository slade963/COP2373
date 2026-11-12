class BankAcct:

    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)
        self.last_interest = 0.0

    def adjust_interest_rate(self, new_rate):
        if new_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = float(new_rate)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if amount > self.amount:
            raise ValueError("Insufficient funds.")
        self.amount -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self.amount += amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        if days < 0:
            raise ValueError("Days cannot be negative.")

        self.last_interest = (
            self.amount * (self.interest_rate / 100) * (days / 365)
        )

        self.amount += self.last_interest
        return self.last_interest

    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Earned: ${self.last_interest:.2f}\n"
            f"Interest Rate: {self.interest_rate:.2f}%"
        )


def test_bank_account():

    account = BankAcct("Jordan Smith", "123456789", 1000.00, 5.0)

    print("Initial Account:")
    print(account)

    account.deposit(250.00)
    print("\nAfter Deposit:")
    print(f"Balance: ${account.get_balance():.2f}")

    account.withdraw(100.00)
    print("\nAfter Withdrawal:")
    print(f"Balance: ${account.get_balance():.2f}")

    account.adjust_interest_rate(6.0)
    print("\nAfter Interest Rate Adjustment:")
    print(f"Interest Rate: {account.interest_rate}%")

    interest = account.calculate_interest(30)

    print("\nAfter Calculating 30 Days of Interest:")
    print(f"Interest Earned: ${interest:.2f}")
    print(account)

    print("\nAll BankAcct tests completed successfully!")


if __name__ == "__main__":
    test_bank_account()