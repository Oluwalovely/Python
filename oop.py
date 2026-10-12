#OOP
# OOP means Object Oriented Programming. It is a programming paradigm that uses objects and classes to structure code. In OOP, we create classes that define the properties and behaviors of objects, and then we create instances of those classes to represent specific objects in our program.

# Is a way of writing program using object and classes. It is a programming paradigm that uses objects and classes to structure code. In OOP, we create classes that define the properties and behaviors of objects, and then we create instances of those classes to represent specific objects in our program.

# Components of OOP
# Inheritance (Class inheritance, object inheritance, multi-class inheritance)
# Encapsulation (Private, Public, Protected)
# Polymorphism, 
# Abstraction

# Classes, Attributes/Properties, Functions/Methods, References, Constructor, Object

# CLASS: It is a python keyword that is used to define a class. A class is a blueprint for creating objects. It defines the properties and behaviors of the objects that will be created from it.

# OBJECT: It is an instance of a class. It is created from a class and has the properties and behaviors defined in the class.

# References: It is a variable that is used to refer to an object. It is used to access the properties and behaviors of the object. It is the first parameter passed to the methods of a class. It is used to access the properties and behaviors of the object.

# class student:
#     student_name = "John"
#     student_age = 20
#     student_course = "Python Programming"
#     student_email = "john@example.com"

#     def take_exams(self, level):
#         print(f"Welcome {self.student_name} to {self.student_course} class, you are in your {level} level")

# stud_1 = student()
# # print(stud_1.student_name)
# # print(stud_1.student_age)
# stud_1.student_name = "Jane"
# stud_1.take_exams("200")
# # print(stud_1.student_name)

# Attributes: It is a variable that is defined inside a class. It is used to store the properties of the objects that will be created from the class.
# import pyttsx3
# engine = pyttsx3.init()
# class car:
#     car_name = "Toyota"
#     car_model = "Corolla"
#     car_year = 2020
#     car_color = "Red"

#     def start_engine(self, price):
#         var = (f"Your {self.car_name} {self.car_model} {self.car_year} engine has started, the price is ${price}")
#         print(var)
#         pyttsx3.speak(var)

#     voices = engine.getProperty('voices')       # getting details of current voice
#     #engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
#     engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

# my_car = car()
# my_car_1 =car()

# my_car.start_engine(20000)



# class Human:
#     species = "Homo sapiens"  # class attribute
#     def __init__(self, name, age, complexion, race, gender):   # object attributes
#         self.user_name = name
#         self.user_age = age
#         self.user_complexion = complexion
#         self.user_race = race
#         self.user_gender = gender

#     def introduce(self):
#         print(f"Hello, my name is {self.user_name}, I am {self.user_age} years old, I have a {self.user_complexion} complexion, I am of {self.user_race} race and I am a {self.user_gender}." )

# first_human = Human("Lamidi", 25, "fair", "Caucasian", "male")
# second_human = Human("Amina", 30, "dark", "African", "female")
# first_human.introduce()
# second_human.introduce()
# print(first_human.introduce())


# ENCAPSULATION
# Encapsulation is the bundling of data and methods that operate on that data within a single unit (class). It restricts direct access to some of an object's components, which is a way of preventing unintended interference and misuse of the data.
# Encapsulation is achieved in Python by using access modifiers. There are three types of access modifiers in Python:
# 1. Public: Members (attributes and methods) declared as public can be accessed from anywhere, both inside and outside the class. By default, all members in Python are public.
# 2. Protected: Members declared as protected can be accessed within the class and its subclasses. In Python, a member is considered protected if its name starts with a single underscore (_).
# 3. Private: Members declared as private can only be accessed within the class itself. In Python, a member is considered private if its name starts with a double underscore (__).
# constructor is the first part of class that is first executed.
# A single underscore (_) before properties makes it becomes protected. It is just a naming convention
# Double underscore (__) before properties makes it becomes private. This actually works and it is more strict than protected. It is a naming convention that makes the property private and it cannot be accessed outside the class.

# class Account:
#     def __init__(self, acct_name, acct_num, acct_balance):
#         self.user_name = acct_name
#         self.user_num = acct_num
#         self.user_bal = acct_balance
#         # self._user_pin = "1234"  # Protected attribute
#         # self.__user_ssn = "123-45-6789"  # Private attribute
#         self.deposit(1000)

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         self.user_bal += amount
#         print(f"Deposit of ${amount} successful. New balance: ${self.user_bal}")

#     def check_balance(self):
#         print(f"Current balance: ${self.user_bal}")


# my_account = Account("John Doe", "123456789", 0.0)
# my_account.deposit(1000)
# if you want to access the protected attribute, you can do so using the following syntax:
# print(my_account._user_pin)  # Accessing protected attribute (not recommended)
# if you want to access the private attribute, you can do so using the following syntax:
# print(my_account.__user_ssn)  # Accessing private attribute (will raise an error) unless you use name mangling like this:
# print(my_account._Account__user_ssn)  # Accessing private attribute using name mangling (not recommended)

# my_account.__user_bal = 500
# print(my_account._Account__user_bal)  # This will not change the actual private attribute due to name mangling
# my_account.check_balance()

# class Father:
#     def __init__(self, first_name, last_name, age, occupation):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.occupation = occupation
#         self.introduce()

#     def introduce(self):
#         print(f"Hello, my name is {self.first_name} {self.last_name}, I am {self.age} years old and I work as a/an {self.occupation}.")

# father_1 = Father("John", "Doe", 45, "Engineer")

# class Son(Father):
#     def __init__(self, first_name, last_name, age, occupation, school):
#         self.school = school
#         super().__init__(first_name, last_name, age, occupation)
#         self.introduce()

#     def introduce(self):
#         print(f"Hello, my name is {self.first_name} {self.last_name}, I am {self.age} years old and I work as a/an {self.occupation}. I attend {self.school}.")
#         # return super().introduce()

# son_1 = Son("Michael", "Doe", 20, "Student", "XYZ University")


# Create a bank app using OOP and inheritance. The class account is the mother class, while class bank inherits from class account. The bank class should have methods for deposit, withdraw, check balance and transfer. The account class should have attributes for account name, account number, account type and account balance. Private attributes should be used for account balance. The bank class should also have a method for displaying the account details.

# import os
# import json


# def get_database():
#     if os.path.exists("bank_db.json"):
#         with open("bank_db.json", "r") as file:
#             return json.load(file)

#     else:
#         db = {
#             "accounts": []
#         }

#         with open("bank_db.json", "w") as file:
#             json.dump(db, file, indent=4)

#         return db


# def save_database(db):
#     with open("bank_db.json", "w") as file:
#         json.dump(db, file, indent=4)

# Multi class inheritance
# class Father:
#     def __init__(self, name, age, occupation, gender):
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#         self.gender = gender

#     def getfather_property(self):
#         print(f"These are the properties I got from my father {self.name}, {self.occupation}, {self.gender}")

# class Mother:
#     def __init__(self, character, skills):
#         self.character = character
#         self.skills = skills

#     def getmother_property(self, skills, character):
#         print(f"I got these properties from my mother: {skills} and {character}")

# mother = Mother("Anger", "cooking")

# class Child(Father, Mother):
#     def __init__(self, name, age, occupation, gender):
#         super().__init__(name, age, occupation, gender)

# child1 = Child("Adeoba", "15", "student", "male")
# child1.getmother_property("cooking", "anger")


# class Account:
#     def __init__(self, acct_name, acct_num, acct_type, acct_balance):
#         self.acct_name = acct_name
#         self.acct_num = acct_num
#         self.acct_type = acct_type
#         self.__acct_balance = acct_balance

#     def get_balance(self):
#         return self.__acct_balance

#     def set_balance(self, new_balance):
#         self.__acct_balance = new_balance


# class Bank(Account):
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be greater than zero.")
#             return

#         current_balance = self.get_balance()
#         new_balance = current_balance + amount
#         self.set_balance(new_balance)
#         print(f"Deposit successful. New balance: ₦{new_balance}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be greater than zero.")
#             return

#         current_balance = self.get_balance()
#         if amount > current_balance:
#             print("Insufficient funds.")
#         else:
#             new_balance = current_balance - amount
#             self.set_balance(new_balance)
#             print(f"Withdrawal successful. New balance: ₦{new_balance}")

#     def check_balance(self):
#         print(f"Your account balance is ₦{self.get_balance()}")

#     def display_account_details(self):
#             print("Account Details")
#             print(f"Account Name: {self.acct_name}")
#             print(f"Account Number: {self.acct_num}")
#             print(f"Account Type: {self.acct_type}")
#             print(f"Account Balance: ₦{self.get_balance()}")

#     def transfer(self, receiver, amount):
#         if amount <= 0:
#             print("Transfer amount must be greater than zero.")
#             return

#         current_balance = self.get_balance()
#         if amount > current_balance:
#             print("Insufficient balance.")
#         else:
#             self.set_balance(current_balance - amount)
#             receiver_balance = receiver.get_balance()
#             receiver.set_balance(receiver_balance + amount)
#             print(f"Transfer successful. ₦{amount} sent to {receiver.acct_name}.")

# my_acct = Bank("Emmie", "12345", "savings", 0.0)
# john_acct = Bank("John", "67890", "Savings", 2000)
# # my_acct.deposit(5000)
# # my_acct.transfer(john_acct, 1000)

# # my_acct.check_balance()
# # john_acct.check_balance()
# # my_acct.display_account_details()
# # my_acct.withdraw(2000)
# # my_acct.check_balance()

# while True:
#     print("""
#         WELCOME TO GIRAN BANK:
#         What do you want to do:
#         1. Deposit
#         2. Withdraw
#         3. Check balance
#         4. Transfer
#         5. Display account details
#         6. Exit
#         """)

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         amount = float(input("Enter amount to deposit: "))
#         my_acct.deposit(amount)

#     elif choice == "2":
#         amount = float(input("Enter amount to withdraw: "))
#         my_acct.withdraw(amount)

#     elif choice == "3":
#         my_acct.check_balance()

#     elif choice == "4":
#         amount = float(input("Enter amount to transfer: "))
#         my_acct.transfer(john_acct, amount)

#     elif choice == "5":
#         my_acct.display_account_details()

#     elif choice == "6":
#         print("Thank you for banking with us.")
#         break

#     else:
#         print("Invalid choice. Please try again.")

# Polymorphism

class Dog:
    def speak(self):
        print("bark")

class cat:
    def speak(self):
        print("meow")

class cow:
    def speak(self):
        print("moo")

animals = [Dog(), cat(). cow()]
for animal in animals:
    animal.speak()


# Abstraction

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_name, account_number, account_type, account_bal):
        super().__init__()
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        self.__account_balance = account_bal




