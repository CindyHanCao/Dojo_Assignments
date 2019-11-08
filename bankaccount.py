class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.intRate = int_rate
        self.account_balance = balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
        
    def display_account_info(self):
        print("Balance: ", self.account_balance)
        return self
    
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance *= (1+self.intRate)
        return self

if __name__ == "__main__":
    first = BankAccount(0.1, 500)                 
    first.deposit(20).deposit(30).deposit(40).withdraw(20).yield_interest().display_account_info()

    second = BankAccount(0.02, 1000)
    second.deposit(200).deposit(300).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()


    