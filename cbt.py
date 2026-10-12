from exam import Exam

class CBT(Exam):
    def __init__(self):
        super().__init__()
        self.main_menu()

    def main_menu(self):
        while True:
            print(f"Welcome to {self.Exam_name}")
            print("""
            1. Take Test
            2. Check Result
            3. Exit
            """)

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter your name: ")
                self.take_test(name)

            elif choice == "2":
                name = input("Enter your name: ")
                self.check_result(name)

            elif choice == "3":
                print("Exiting CBT app...")
                break

            else:
                print("Invalid choice")


cbt = CBT()