class BankAccount:
    acct_id: int
    first_name: str
    last_name: str
    balance: float

    # constructor method
    def __init__(self, acct_id, first_name, last_name):
        # establish & set the attributes
        self.acct_id = acct_id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.00

    # method to print out a string
    def __str__(self):
        s = (f"Account #{self.acct_id} belonging to {self.first_name} {self.last_name} "
                f"has a balance of ${self.balance:.2f}")
        return s

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError(f"Account #{self.acct_id} only has ${self.balance:.2f} left.")

    def transfer_from(self, amount, to_acct_id):
        try:
            self.withdraw(amount)
            to_acct_id.deposit(amount)
        except ValueError:
            print(f"As expected, transfer failed: Account #{self.acct_id} only has ${self.balance:.2f} left.")

    def set_first_name(self, new_name):
        self.first_name = new_name

    def set_last_name(self, new_name):
        self.last_name = new_name

    def get_balance(self):
        return self.balance

    def get_fullname(self):
        return self.first_name + ' ' + self.last_name

    def __add__(self,right_operand):
        total = self.balance + right_operand.balance
        return total


def main():
    print("Welcome to Bank of Pawnee!")

    acct1 = BankAccount(8105, 'Leslie', 'Knope')
    acct2 = BankAccount(2816, 'Ben', 'Wyatt')
    print(acct1)
    print(acct2, '\n')

    acct1.deposit(100)
    acct2.deposit(100)

    print("DEPOSITING...")
    print(acct1)
    print(acct2, '\n')

    #test that works
    print('WITHDRAWING...')
    acct1.withdraw(10.00)
    print("$10 from Leslie's account")
    print('Now,',acct1, '\n')

    print("Attempting to now withdraw $101.50 from Ben's account...")
    #test DOESN'T work
    try:
        acct2.withdraw(150.00)
    except ValueError as e:
        print("As expected, there is not enough money")
        print('Exception:', e,'\n')

    # test that works
    print('TRANSFERRING...')
    acct1.transfer_from(50.00, acct2)
    print("$50 from Leslie's account to Ben's.")
    print(f'Which leaves Leslie with ${acct1.get_balance():.2f} and')
    print(f'Ben with ${acct2.get_balance():.2f}')

    # test DOESN'T work
    print("\nAttempting to now transfer $350.45 from Leslie's account to Ben's...")
    acct1.transfer_from(350.45, acct2)
    print(acct1)
    print(f'and Ben Wyatt with ${acct2.get_balance():.2f}. (No change to balance)\n')

    print('UPDATING NAME...')
    acct2.set_first_name('Calzone-Boy')
    print('Showing the updated first name,',acct2)

    acct1.set_last_name('Knope-Wyatt')
    print('Showing the updated last name,',acct1, '\n')

    print('INDIVIDUALLY...')
    print(f"{acct1.get_fullname()}'s balance is: ${acct1.get_balance():.2f}")
    print(f"{acct2.get_fullname()}'s balance is: ${acct2.get_balance():.2f}")

    print('\nCOMBINED...')
    total = acct1 + acct2
    print(f"{acct1.get_fullname()} and {acct2.get_fullname()} both have a total balance of ${total:.2f}\n")


main()