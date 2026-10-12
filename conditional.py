# Conditional Statements
# if, elif, else
# x = 5
# if x == 5:
#     print("statement is true")
# elif x < 0:
#     print("statement is false")
# elif x > 10:
#     print("statement is false")
# else:
#     print("watin be this one like this")
# Assignment: Build a USSD application with conditional statement.

# Nested conditional statement
# x = 5
# y = 20

# if x == 5:
#     if y < 10:
#         print("Both statements are True")
#     else:
#         print("First statement is true")
# else:
#     print("Both statements are false")

# name = "Emmie"
# age = 35

# if age >= 18:
#     if age < 80:
#         print("You are eligible to vote")
#     else:
#         print("You are too old to vote")
# else:
#     print("You are too young to vote")


ussd = input("Enter your USSD: ")
if ussd == "*312#":
    print("""
    1. Data plans
    2. Enjoy 18gb for 4k
    3. Voice plans
    4. Gift data
        """)
    choice = input("Enter your choice: ")
    if choice == "1":
        print("""
            1. Daily
            2. 2 to 3 days
            3. Weekly
            4. 2 weeks
            5. Monthly
            """)
        data_choice = input("Choose a data plan: ")

        if data_choice == "1":
            print("Daily data plans selected.")
        elif data_choice == "2":  
            print("2 to 3 days data plans selected.")
        elif data_choice == "3":
            print("Weekly data plans selected.")
        elif data_choice == "4": 
            print("2 weeks data plans selected.")
        elif data_choice == "5":
            print("Monthly data plans selected.")
        else:
            print("Invalid data plan choice.")

    elif choice == "2":
        print("18 GB for N4,000, valid for 30 days.")
        confirm = input("Enter 1 to buy or 2 to cancel: ")

        if confirm == "1":
            print("Your purchase of 18 GB for N4,000 was successful.")
        elif confirm == "2":
            print("Transaction cancelled.")
        else:
            print("Invalid choice.")

    elif choice == "3":
        print("""
            1. Daily voice plan
            2. Weekly voice plan
            3. Monthly voice plan
            """)
        voice_choice = input("Choose a voice plan: ")

        if voice_choice == "1":
            print("Daily voice plan selected.")
        elif voice_choice == "2":
            print("Weekly voice plan selected.")
        elif voice_choice == "3":
            print("Monthly voice plan selected.")
        else:
            print("Invalid voice plan choice.")

    elif choice == "4":
        phone_number = input("Enter the recipient's phone number: ")
        data_amount = input("Enter the amount of data to gift (for example, 500MB): ")
        confirm = input(
            f"Gift {data_amount} to {phone_number}? Enter 1 to confirm or 2 to cancel: "
        )

        if confirm == "1":
            print(f"You successfully gifted {data_amount} to {phone_number}.")
        elif confirm == "2":
            print("Transaction cancelled.")
        else:
            print("Invalid choice.")

    else:
        print("Invalid menu choice.")
else:
    print("Invalid USSD code.")
