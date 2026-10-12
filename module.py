# Modularization

class Account:
    Bank_name = "Pennywise MFB" #class attributes
    def __init__(self, account_name, account_number, account_type, account_bal): #instance attribute or object attribute
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        self.__account_balance = account_bal

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            # return
        self.__account_balance += amount
        print(f"Deposit of {amount} successful, your new balance is {self.__account_balance}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Cannot withdraw zero")
            return
        if amount > self.__account_balance:
            print("Insufficient funds")
            return
        self.__account_balance -= amount
        print(f"Withdraw of {amount} successful, your balance is {self.__account_balance}")

    def check_balance(self):
        return self.__account_balance