# Conditional Statements
# if, elif, else
x = 5
if x == 5:
    print("statement is true")
elif x < 0:
    print("statement is false")
elif x > 10:
    print("statement is false")
else:
    print("watin be this one like this")
# Assignment: Build a USSD application with conditional statement.

# Nested conditional statement
x = 5
y = 20

if x == 5:
    if y < 10:
        print("Both statements are True")
    else:
        print("First statement is true")
else:
    print("Both statements are false")

name = "Emmie"
age = 35

if age >= 18:
    if age < 80:
        print("You are eligible to vote")
    else:
        print("You are too old to vote")
else:
    print("You are too young to vote")


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