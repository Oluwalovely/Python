from module import Account

class Bank(Account):
    def __init__(self, account_name, account_number, account_type, account_bal):
        super().__init__(account_name, account_number, account_type, account_bal)
        self.main_menu()

    def main_menu(self):
        while True:
            print("""
            1. Deposit
            2. Withdraw
            3. Check balance
            4. Transfer
            5. Exit
            """)

            choice = input("Enter choice: ")

            if choice == "1":
                self.deposit(500)

            elif choice == "2":
                self.withdraw(200)

            elif choice == "3":
                print(f"Your balance is: {self.__account_balance()}") 

            elif choice == "5":
                print("Exiting bank app, bye.....")
                break



user1 = Bank("Emmie", "123456789", "savings", 0.0)