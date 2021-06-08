from  BankAccount import BankAccount as BA 
class User:
    def __init__(self,name,int_rate=2,balance=0):
        self.name=name
        self.bank_account = BA(int_rate,balance)
    def make_withdrawal(self, amount):
        self.bank_account.withdraw(amount)
        return self
    def make_deposit(self, amount):
        self.bank_account.deposit(amount)
        return self
    def display_user_balance(self):
        self.bank_account.display_account_info()
        return self
    def  transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount
        return self

dipinder = User("dipinder",balance=1000)
dipinder.make_deposit(200).make_withdrawal(100).display_user_balance()