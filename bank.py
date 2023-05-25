class Account:
    type = "Savings"
    def __init__(self,number, password, loan_balance, deposits):
        self.balance = 0
        self.number = number
        self.password = password
        self.deposits = deposits
        self.withdrawals = []
        self.loan_balance = loan_balance
    
        
    def deposit(self, amount):
        transaction = self.create_transaction(amount)
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        transaction = self.create_transaction(amount)
        self.withdrawals.append(transaction)

    
    def check_balance(self, amount):
        total_deposits = 0
        total_withdrawals = 0

        for amount in self.deposits:
            total_deposits += amount

        for amount in self.withdrawals:
            total_withdrawals += amount

        return total_deposits - total_withdrawals

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        total_deposits = sum(transaction['amount'] for transaction in self.deposits)
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= total_deposits / 3:
            self.loan_balance += amount
            print("Loan has been approved!")
        else:
            print("Loan request has been denied.")

    def repay_loan(self, amount):
        if self.loan_balance > 0:
            if amount >= self.loan_balance:
                self.loan_balance = 0
                extra_payment = amount - self.loan_balance
                self.deposits(extra_payment)
                print("Loan needs to be fully repaid!")
            else:
                self.loan_balance -= amount
                print("Loan has been partially repaid.")
        else:
            print("No outstanding loan to repay.")

    def transfer(self, amount, recipient_account):
        current_balance = self.balance()
        if amount <= current_balance:
            self.withdrawal(amount)
            recipient_account.deposits(amount)
            print("Transfer is successful!")
        else:
            print("Insufficient balance for transfer.")

          