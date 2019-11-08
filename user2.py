class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposits(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: ", self.name, "Balance: ", self.account_balance)
        return self



cindy = User("Cindy", "cc@email.com")
han = User("Han", "hh@email.com")
naonao = User("Naonao", "nn@email.com")

cindy.make_deposits(50).make_deposits(10).make_deposits(50).make_withdrawal(30).display_user_balance()


han.make_deposits(200).make_deposits(200).make_withdrawal(200).make_withdrawal(200).display_user_balance()

naonao.make_deposits(200).make_withdrawal(10).make_withdrawal(20).make_withdrawal(50).display_user_balance()







