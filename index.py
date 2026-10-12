# print("Welcome to python class")

# print(2+3)
# print(2**2)

# x = int(5)
# print(type(x))
# x.

# x = "5"
# x.
# import random as rd
# print("Ade is a \"boy"")
# print("Ade is a 'boy'")
# rd.r

# four module
# module 1:
# indentation
# commenting
# data types
# python operatiors
# conditional statements
# python collections and arrays
# x = 5
# if x > 4:
# print(x)
# x = 5
# y = 10
# if x > y:
#     print("x is greater than y")
# else:
#     print("x is not greater than y")

# commenting
# multi level commenting
# """
# This is Registrtation page
# """
# print("Thank you")
# python variables
# variables are containers where we keep our data types in python
# x = 5
# rules of variable declarations
# 1. All varables must start with either an underscore or chracters
# var = 5
# _var = 5
# print(_var)
# 9999var = 5
# 2. varibles are case sensitive
# age = 5
# Age = 10
# print(age)
# print(Age)

# 3. varibales cannot include space in between
# first name = "Ogunfumi"
# print(first name)

# 4. varibles must not include python keywords
# def = "fortune"
# print(def)
# print = "output"

# multiple varibale to multiple values decalration
# x,y = 5,6
# print(type(x))
# print(y)
# multiple variable to a single value declaration
# x = y = z = 60
# print(x)
# print(y)
# print(z)
# first_fruit, *second_fruit, last_fruit = ["orange", 'apple', 'mango', "strawberry", "banana"]
# print(first_fruit)
# print(second_fruit)
# fruits =  ["orange", 'apple', 'mango', "strawberry", "banana"]
# print(fruits[-1])

# python input
# python output
# concatination
# casting

# name =  input("what is your name: ")
# print("my name is ", name)

# x = int(input("enter your first number: "))
# y = float(input("enter your second number:  "))
# print(x + y)
# print(type(x))
# print(type(y))

# x = str(5)
# print(type(x))
# concatination
# contination is the method of adding varibles to a collection strings values
# 1. using the addition operator
# 2. using the formation strings
# 3. concatinate using the .join function


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# year_of_birth = 2026-age
# # print("my name is " + name + " " + "and I am" + " " + age + " " + "years old" )
# print(f"My name is {name} and I am {age} years old and I was born in {year_of_birth}")

# assignment
# concatenate using .join
# create a registration form and recieve the inpuy of the users then print out the recieve generatimg account number for the user.

# import random as rd
# account_number = rd.randint(1000000000, 999999999)
# print(account_number)

# introduction to python data types
# 1. text type
# strings
# 2. number data types
# int, float, complex

# 3. boolean data types
# true, false
# sequence datatypes
# list, tuples, range
# mapping datatypes
# dictionary, sets
# binary datatypes
# sets data type
# x = {"annie","chris","mubq","tolu"}
# bytes, bytearray, memoryview
# none data type

# gender  = "female"
# print(type(gender))
# print(gender.capitalize())
# print(gender.upper())
# constructor = str()
# x = range(1,100)
# # print(list(x)) #casting#
# y =list(x)
# print(type(y))
# # x = 6.0
# print(type(x))
# {"name":"Annie"}

# x = 4 + 5j
# print(type(x))

# x = 44E5
# print(type(x))

# cars = ["rolls royce", "benz", "lambo", "lexus", "porshe", "benz", "bmw"]
# list properties:
# list can indexed
# list is mutable
# list are ordered
# print(type(cars))
# print(cars[0])
# cars[0] = "keke napep"
# print(cars)
# print(cars[0:5])
# print(cars[2:])
# print(cars[-1])
# print(cars[-3:-1])
# print(len(cars))

names = ("kenny", "fawaz", "fortune", "harmony", "christianah", "anne", "mubaraq", "christianah")
# tuples properties
# tuples can be indexed
# tuples are not mutable, which means the items in tuple cannot be changed
# tuples are ordered
# tuples allow duplicate values 
# print(names)
# print(type(names))
# print(names[0])
# names[0] = "Taiwo"
# print(names)
# print(names[0:5])
# print(names[-1])
# print(names[-3:-1])
# print(names)

# dictionaries
# properties
# dictionaies are represented in keys and values

# user = {
#     "name": "kenny",
#     "Age": 30,
#     "course": "Artificial intelligence",
#     "gender": "male",
#     "address": {
#         "street":"Golf street",
#         "Area": "Ogooluwa Area"
#     }
    
    
# }
# print(user)
# print(type(user))
# print(user["name"])
# print(user["name"], user["Age"])
# user["name"] = "fawaz"
# print(user["address"]["street"])
# print(user["address"]["Area"])
# user.
# try:

#     user["name":"address"]
# except Exception as e:
#     print(e)
# range
# casting
# x = range(0, 100)
# x = range(0, 100, 5)
# print(list(x))

# sets

# collection of unique elements

banks = {"opay", "palmpay", "moniepoint", "opay", "kuda", "paga"}
# print(type(banks))
# print(banks)
# sets are unordered
# sets are cannot be indexed
# sets are not mutable
# sets does not accept duplicate values

# print(banks[0])
# banks[0] = "gtbank"
# print(banks)

# banks.
# x = b"Hello"
# print(type(x))
# x = ord("e")
# y = chr(80)
# print(x)
# print(y)

# operators
# Arithmetic operators
# 1. addition. subtraction, division, multiplication, modulus, floor division, exponontia
# walrus operator
# x = 5
# y = 10
# print(x + y)
# print(x - y)
# print(x * y)
# print(x ** y)
# print(x / y)
# print(x // y)
# print(x % y)

# comparison operator
# >, <, ==,  <=, !=, >=

# x = 6
# y = 7
# print(x > y)
# print(x < y)
# print(x==y)
# print(x >= y)
# print(x <= y)
# print(x != y)
# x = range()
# score = 89
# if (score:=50) >= 70 and score <= 100:
#     print(score)
#     print("A")
# elif score >= 60 and score <= 69:
#     print("B")
# else:
#     print("Invalid score, you be mumu")

# score = int(input("Enter score: "))
# if score in range(70, 100):
#     print("A")
# elif score in range(60, 69):
#     print("B")
# elif score in range(50, 59):
#     print("c")
# elif score in range(45, 49):
#     print("D")
# elif score in range(40, 44):
#     print("E")
# elif score in range(0, 39):
#     print("F9")
# else:
#     print("Invalid score")
# logical operator
# and, or not
# or
x =  6
y = 200

# if x >= 5 and y >= 130:
#     print("Valid")
# else:
#     print("Invalid")

# if x > 10 or y < 20:
#     print("Valid")
# else:
#     print("Invalid")



# if not(x >= 5 and y >= 130):
#     print("Valid")
# else:
#     print("Invalid")

# if not( x > 10 or y < 20):
#     print("True")
# else:
#     print("False")

# membership operator
# in, not in

# berries = ["strawberry", "blackberry", "blueberry", "raspberry", "redberry", "craneberry"]
# berries = ("strawberry", "blackberry", "blueberry", "raspberry", "redberry", "craneberry")
# if "blackberry" in berries:
#     print("Found")
# else:
#     print("Not found")


# if "cherry" not in berries:
#     print("Found")
# else:
#     print("Not found")

# assignment operator
# -=, +=, *=, \=, \\=, **=, %=, :=, <<=,>>=

# x = 5
# x += 10
# print(x)
# x = x + 10
# print(x)

# x -= 10
# print(x)

# if x := 10:
#     print(x)
# iif 
# x = 10
# if x == 10:
#     print(x)
# if x:= 10 :
#     print(x)

# assignment
# if x <= 20

# identity
# is, is not
# x = 100
# y = 100
# a = [100, 200, 300, 400]
# b = [100, 200, 300, 400]
# # print(x is y)
# # print(x == y)
# print(a is b)
# print(a == b)
# print(id(x))
# print(id(y))
# print(id(a))
# print(id(b))

# bitwise opearator
# &|^~
# x = 90 & 7
# print(~x)
# print(90 & 7)
# print(90 | 7)
# print(90 ^ 7)
# print()
# x = bin(90)
# print(x)
# print(bin(~90))
# conditional statements
# three blocks of conditonal staments
# 1. if, elif, else

# if x > 10:
#     print("statement is true")
# elif x < 0:
#     print("x is less than 100")
# elif x == 50:
#     print("x is same as 5")
# else:
#     print("Wetin be this")
# build a ussd application with conditinal statement
# with operations
# nested conditional statemnt.
# x = 5
# y = 20
# if x == 50:
#     if y > 10:
#         print("Both statement are true")
#     else:
#         print(" only first statement is true ")
# else:
#     print("Both statement are false")
# name = "Tolu"
# age = 8

# if age >= 18:
#     if age < 80:
#         print("You are eligible to vote")
#     else:
#         print("You are too old pls go home and pray for the country")
# else:
#     print("You are too young to vote")

# ussd = input("Enter your ussd: ")
# if ussd == "*312#":
#     print("""
#     1. Data plans
#     2. Enjoy 18gb for 4k
#     3. voice overs
#     4. Gift data
#         """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print("""
#             1. Daily
#             2. 2 to 3 days
#             3. weekly
#             4. 2 weeks
        
#             """) 
# expression, iteration, iterate and iterable
# break and continue, pass
# fruits  = ["berry", "orange", "banana", "melon","cherry"]
# for i in fruits:
#     print(i)
#     if i == "melon":
#         break
#     print("found")
# print("="*60)

# for x in fruits:
#     print(x)
#     if x == "melon":
#         continue
#     print("found")

# for annie in fruits:
#     print(annie)
#     # continue
#     if annie == "melon":
#         # print("melon is found")
#         continue
#         print("close end")
# # nested loop
# # for i in range(1, 13):
# #     print(f"Multiplication table {i}")
# #     for x in range(1, 13):
# #         print(f"{i} * {x} = {i*x}")
# #         break

# voting system
# loops
# for loops
# while loops
# x = 1
# while x < 10:
#     print(x)
#     x += 1
# fruits  = ["berry", "orange", "banana", "melon","cherry"]
# print(len(fruits))
# i = 0
# while i < len(fruits):
#     x = fruits[i]
#     print(x)
#     if x == "melon":
#         break
#     i += 1
# x = "fortune"
# if x:
#     print(x)
# create a list of items
# loop over the list 
# stiop the loop when its get to a particular itme in the list
# python collections and array

# x = "banana"
# # x.capitalize
# print(type(x))\
# fruits = ["banana", "apple"]
# fruits.
# import calendar
# print(calendar.calendar(2026))
# solid principles
# print("Welcome to sqi cinema")
# tickets = 5
# vip_ticket = 2
# while tickets > 0:
#     name = input("Enter your name: ")
#     age  = int(input("Enter your age: "))
#     if age < 18:
#         print("You are too young for this, go and watch animie")
#         break
#     print("Ticket available")
#     print("""
#         1. Regular
#         2. VIP
#         """)
#     option = input("Which ticket do you want: ")
#     if option == "1":

#         print("""Welcome to The Home of Fortune,
#             choose the film to watch below:
#                 1. Anne
#                 2. Ninja
#                 3. spiderman
            
#                 """)
#         choice = input("Enter your choice")
#         if choice == "1":
#             print("Go to room 4, for regular section")
#             tickets -= 1
#             print(f" selling out soon, {tickets} tickets remaining, you can purchase for your loved ones")
#             continue
#     elif option == "2":
#         if vip_ticket < 1:
#              print("No more vip ticket, you can only purchase regular")
#              continue
#         print("""Welcome to The Home of Fortune,
#                     choose the film to watch below:
#                         1. Anne
#                         2. Ninja
#                         3. spiderman
                    
#                         """)
#         choice = input("Enter your choice")
#         if choice == "1":
#             print("Go to room 5, for vip section")
#             vip_ticket -= 1                  
# else:
#     print("No more ticket")
    # if tickets == 3:
    #     print("no more ticket for regular, only vip")
#     #     break
# i = 0
# while i > 0:
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         print(type(i))
#         continue
#     print(i)
# task_db = []
# while True:        
#     print("""Task management system
#         1. Add task
#         2. View task
#         3. Edit task
#         4. Delete task

#         """)
#     choice = input("Enter choice: ")
#     if choice == "1":
#         task_name = input("Enter task: ")
#         task_start_date = input("Enter task date: ")
#         task_deadline = input("Enter task deadline: ")
#         task_desc = input("Enter task desc: ")
#         save_task = {
#             "task_name":task_name,
#             "task_start_date": task_start_date,
#             "task_deadline": task_deadline,
#             "task_description": task_desc
#         }
#         task_db.append(save_task)
#         harmony = task_db[0]
#         print(f"""
#             task :  {harmony["task_name"]}
#             date : {harmony["task_start_date"]}
#             deadline : {harmony["task_deadline"]}
#             description : {harmony["task_description"]}


#                 """)
#     elif choice == "5":
#         print("Goodbye.....")
#         break
#     else:
#         print("Invalid choice")
#         break




# python collection and arrays
# strings
# name = "tolu"

# user_name = input("Enter name: ")
# if name == user_name.casefold():
#     print("User found")
# else:
#     print("User not found")
# x = "12'%'%'^BAN_ANA..//kkl"
# itm = ["banana", "mango", "watermelon"]
# x = "Banana is a type of fruit"
# x = "//////banana//////"
# x = "banana"
# print(x.capitalize())
# print(x.casefold())
# print(x.capitalize())
# print(x.center(20, "*"))
# print(x.casefold().count("a"))
# print(x.count("A",0, 6))
# print(type(x.encode()))

# print(x.endswith("b"))

# print(x.expandtabs())

# print(x.find("A", 4))

# print(x.format())

# print(x.index("A"))

# print(x.isalnum())
# print(x.isascii())
# print(" ".join(itm))
# dundee
# print(x.split(" "))
# print(x.split(''))

# print(x.strip("/"))
# print(x.lower())
# print(x.title())
# print(x.upper())

# list methods

# fruits = ["banana", "apple", "cherry", "strawberry", "orange"]

# print(fruits.index("apple"))
# print(fruits.count("cherry"))
# print(fruits)
# print(fruits.append("mango"))
# new_fruits = fruits.copy()
# print(new_fruits)
# fruits.extend(["watermelon, orange"]) 
# # print(fruits)
# fruits.insert(2, "guava")
# print(fruits)
# print(fruits.pop())
# fruits.pop(0)
# fruits.remove("apple")
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)
# fruits.clear()
# fruits.reverse()
# print(fruits)

# print(fruits)

# cars = ["bmw", "porshe", "lambo", "benz", "lexus"]
# price = ["19m", "50m", "350m", "25m", "15m"]

# for each_car, each_price in zip(cars, price):
#     print(f"{each_car}: {each_price}")
# result_db = []
# questions = [
#     "what is the county with the most island in the world",
#     "what is the country highest curreny rate",
#     "what is the country with the best president",
#     "what is the country with the highest population",
# ]

# answer = [
#     "sweden",
#     "kuwait",
#     "Nigeria",
#     "china"
#     ]
# while True:
#     print("""
#         welcome to sqi cbt
#         1. Take exams
#         2. check result
#         3. exit
#         """)
#     choice = input("Enter youir choice: ")
#     if choice == "1":
#         name = input("Enter your name: ")
#         score = 0
#         for each_ques,each_ans in zip(questions, answer):
#             print(each_ques)
#             user_ans = input("Enter your answer: ")
#             if user_ans.casefold().strip(" ") == each_ans.casefold():
#                 score += 1
#                 print("Correct")
#             else:
#                 print("Olodo rabata") 
#         # print(f"{name}, You score: {score}/{len(questions)} ")
#         users_details = {
#                 "name": name,
#                 "score": score
#             }
#         result_db.append(users_details)
#     elif choice == "2":
#         # each_user_res = result_db[0]
#         name = input("Enter name: ")
#         # if name == each_user_res["name"]:
#         #     print(f"{name}, you score {each_user_res["score"]}")
#         # else:
#         #     print("Result not found!!!")
#         for each_user in result_db:
#             if name == each_user["name"]:
#                 print(f"{each_user["name"]}, you score : {each_user["score"]}")

#         # print("Result not available")

        
#     elif choice == "3":
#         print("Exiting.......")
#         break

# questions = {
#     "What is the country with the most islands in the world?": "Sweden",
#     "What is the country with the highest currency rate?": "Kuwait",
#     "What is the country with the best president?": "Nigeria",
# }
# # questions.update(status="Active")
# questions.update({"who is the best student": "Miss tolu"})
# questions.update(who_is_the_manager_of_sqi="Miss Bam")
# print(questions)

# funtions
# funtion definition,
# funtion declaration
# funtion invocation

# unparametised funtion

# def introduce(age, name="Student"):
#     # print("Welcome christinah")
#     # name = "harmony"
#     print(f"Welcome {name}, you are {age} years old")
# introduce("Toluwanimi")
# # introduce("Fawaz")
# # introduce("fortune")
# introduce(21, "harmony")

# def add(val1, val2):
#     return val1 + val2
# result = add(5,5)
# print(result)

# keyword argument and positional argument
# positional argument
# def introduce(age, name):
#     return f"Welcome {name}, you are {age} years old"
# res = introduce("christy", 35)
# print(res)
# # keyword argument
# def introduce(age, name):
#     return f"Welcome {name}, you are {age} years old"
# res = introduce(name ="christy", age=35)
# print(res)

# *args and **kwargs
# local varibale anf global variable
# questions = {
#     "What is the country with the most islands in the world?": "Sweden",
#     "What is the country with the highest currency rate?": "Kuwait",
#     "What is the country with the best president?": "Nigeria",
# }
# def student_portal():
#     print("""
#         1. Take exams
#         2. check_result
#         3. exit
#             """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         take_exams("Easy")
#     elif choice =="2":
#         pass
#     elif choice == "3":
#         exit()
# def take_exams(name):
#     print(f"Welcome {name}")
#     for indx, each in enumerate(questions.items(), start=1):
#         print(f"{indx}: {each[0]}")
#         user_ans = input("Enter your answer: ")
#         if user_ans.casefold().strip(" ") == each[1].casefold():
#             print("correct") 
#         else:
#             print("wrong")


# while True:
#     print("""
#         1. student portal
#         2. Teacher portal
#         3. Exit
#         """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         student_portal()
#     elif choice == "2":
#         pass
#     elif choice == "3":
#         print("Byeeeeee.....")
#         exit()
#     else:
#         print("Invalid input")

# positional-only and keyword-only arguments
# def welcome_user(greet, name):
#     # return f"{greet} {name}, you are welcome"
#     print(f"{greet} {name}, you are welcome")
# welcome_user(greet="HEllo", name="emma")

# positiona-only
# def welcome_user(greet, name, /):
#     return f"{greet} {name}, you are welcome"
# print(welcome_user(greet="Hello", name="Tolu"))

# keyword-only
# def welcome_user(*,greet, name):
#     return f"{greet} {name}, you are welcome"
# print(welcome_user(greet="Hello", name="fawaz"))

# *args and *args, **kwargs
# name = "toluwani",
# print(name)
# args means arbitrary arguments
# def create_account(*user):
#     print(f"""
#         Welcome {user[0]}
#         you are {user[1]} years old.
#         your mail is {user[2]}
#         """)
# create_account("emma", "21", "emma@gmail.com")
# def intrro(greet,names):
#     for name in names_list:
#         print(f"{greet}, Welcome {name}")

# names_list= ["Mubaraq", "emma", "fawaz(goat)", "kenny","fortune", "harmony"]
# intrro("Hello",names_list)

# **kwargs
# def create_account(greet, **details):
#     # print(details["name"])
#     print(f"{greet}, {details}")
# create_account("Hello", name="fawaz", age=25, course="Python")

# def create_user(**details):
#     print(f""" welcome
#     {details["name"]}
#     {details["age"]}
#     {details["course"]}
#         """)
# user_details ={"name": "fawaz", "age": 24, "course":"python"}
# create_user(user_details)
# ketword only and positionly
# def beginning(val1,val2, /, *,val3,val4 ):
#     return val1+val2, val3*val4
# print(beginning(3, 2, val4=5,val3=6))

# def max_score(*scores):
#     max_score = scores[0]
#     for num in scores:
#         if num > max_score:
#             max_score = num
#     return max_score
# print(max_score(1,4,5,8,9,2))

# introduction to json

# javascript object notation

# import json
# data = [{
#     "name": "fawaz",
#     "age": 21
# }]
# print(type(data))
# fil = json.dumps((data))
# print(fil)
# print(type(fil))
# with open("databases.json", "w") as file:
    # file.write("Toluwani is a good girl")
    # f = file.readline()
    # print(f)
    # json.loads(file)
    # json.dump([{"name": "Tolu"}])
# 
# dump file with json
# with open("data.json", "w") as file:
# #     # json.dump([{"name": "Tolu"}])
#     json.dump([{"course": "python"},
#                 {"age": 23},
#                 {"occupation": "gbepawo"}
#                 ], file, indent=4)

# load json
# with open("data.json", "r") as file:
#     print(json.load(file))
# # with 

# with open("database.json", "w") as file:
#     json.dump(data, file)


# # simple task management system
import json
import os
import datetime as dt
import pyttsx3
# import functools
loggin = False
# python decorators
def login_required(func): 
    def wrapper(*args, **kwargs):
        if loggin == False:
            print("You must be logged in to access this function.")
            return
        return func(*args, **kwargs)
    return wrapper
# print(dt.datetime.now().strftime("%H:%M"))
# print(dt.datetime.now())

def getdatabase():
    if os.path.exists("task_db.json"):
        with open("task_db.json", "r") as file:
            return json.load(file)
    else:
        with open("task_db.json", "w") as file:
            json.dump([], file, indent=4)
        return []
# getdatabase()
def save_db(user_details):
    with open("task_db.json", "w") as file:
        json.dump(user_details, file, indent=4)


def create_account():
    db = getdatabase()
    print("Welcome register your account")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your mail: ")
    password = input("Enter your password")
    confirm_password = input("Enter  confirm_password:  ")

    for users in db:
        if users["email"] == email:
            print("Email already Exist")
            create_account()
            return
        
    if password != confirm_password:
            print("Password do not match")
            create_account()
            return

    user_details = {
        "name": name,
        "age": age,
        "email": email,
        "password": password,
        "task": []
    }
    db.append(user_details)
    save_db(db)
    print("Account created successfully!!!")
# create_account()
def login_account():
    db = getdatabase()
    print(" Login your account")
    email = input("Enter mail: ").strip().casefold()
    password = input("Enter your password: ").strip().casefold()

    for user in db:
        if user["email"] == email and user["password"] == password:
            global loggin
            loggin = True
            print("Login successful")
            Dashboard(user)
            return
    print("Invalid credentials")
@login_required
def Dashboard(user):
    while True:

        print(f"""Welcome {user["name"]} to dashboard
        1. Add task
        2. View task
        3. edit task
        4. delete task
        5. sort task
        6. completed task
        #. exit
        
        """)
        choice = input("Enter choice: ")
        if choice == "1":
            Add_task(user)
        elif choice == "2":
            view_task(user)
        elif choice == "3":
            edit_task(user)
        elif choice == "#":
            exit()
# Dashboard(user)
# login_account()
def Add_task(user):
    db = getdatabase()
    task_name = input("Enter your task: ")
    task_time = input("Enter the due time: ")
    start_time = dt.datetime.now().strftime("%H:%M")
    task_desc = input("Enter description: ")

    user_tasks = {
        "task_name": task_name,
        "task_time": task_time,
        "start_time": start_time,
        "task_desc": task_desc
    }
    user["task"].append(user_tasks)
    for each in db:
        if each["email"] == user["email"]:
            each["task"] = user["task"]
            break
    save_db(db) 
def view_task(user):
    db = getdatabase()
    if len(user["task"]) == 0:
        print("No task found")
        view_task()
        return

    for index, each in enumerate(user["task"], start=1):
            print( f""" task {index}
                 {each["task_name"]}
                {each["task_time"]}
                 {each["start_time"]}
                {each["task_desc"]}

                    """
                )
    # Dashboard(user)

def edit_task(user):
    db = getdatabase()
    if not user["task"]:
        print("No task available")
        edit_task(user)
        return
    view_task(user)
    ed_idx = int(input("Enter the task number to edit: "))-1
    task_name = input("Enter task name: ")
    task_time = input("Enter task time: ")
    task_description = input("Enter task description: ")
    task = user["task"][ed_idx]

    if task_name:
        task['task_name'] = task_name
    if task_time:
        task["task_time"] = task_time
    if task_description:
        task["task_desc"] =  task_description

    for each in db:
        if user["email"] == each["email"]:
            each["task"]= user["task"]
            break
    save_db(db)
    print(user["task"])
    print("task updated successfully")

    
    
    
    
def main_menu():
    while True:
        print("""
        1. Register
        2. Login
        3. Exit
            """)

        choice = input("Enter choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login_account()
        elif choice == "3":
            print("Bye")
            break 
    

# main_menu()
# x = input("Enter your name: ")
# if x:
#     print(x)
# Dashboard()


# what is class
# x = int()
# x.
# print(type(x))
# class _All_student:
#     student_name = "Victor"
#     student_age =  35
#     student_course = "data analysis"
#     student_mail = "vic@Hotmail.com"

#     def take_exams(self, level):
#         print(f"Welcome {self.student_name} to {self.student_course} class, you are in your {level} level")
# stud_1 = _All_student()
# # print(stud_1.student_age)
# # print(stud_1.student_name)
# stud_1.student_name = "Mafolasere"
# stud_1.take_exams("200")
# # print(stud_1.student_name)
# stud_1.
# # print(type(stud_1))
# import pyttsx3
# # pyttsx3.
# class car:
#     car_name = "Benz"
#     car_model = "GLE"
#     yop = 2020
#     color =  "Black"

#     def start_engine(self):
#         var = f"starting the engine of {self.car_name},{self.car_model} produced in {self.yop} "
#         print(var)
#         pyttsx3.speak(var)

# car_1 = car()
# car_2 = car()
# car_1.engine_type = "v8"
# car_2.engine_type = "v5"
# print(car_1.engine_type)
# print(car_2.engine_type)
# car_1.start_engine()
# constructor
# class Human():
#     species = "Homo sapiens"
#     def __init__(self, name, age, complexion, race, gender):
#         self.user_name = name
#         self.user_age = age
#         self.user_complexion = complexion
#         self.user_race = race
#         self.user_gender = gender
#     def introduce(self):
#         print(f"Welcome {self.user_name}, you are {self.user_age} year old of {self.user_race} race, of {self.species}")

# first_human = Human("emma", "26", "dark", "black", "male")
# # print(first_human.user_name)
# first_human.user_name  = "Tolu"
# print(first_human.user_name)
# second_human = Human("harmony", "16", "light", "black","male")
# # print(first_human)
# first_human.introduce()
# second_human.introduce()

# components of oop
# encapsulation
# public, protetected and private

class Account:
    def __init__(self, acct_name, acct_num, acct_balance):
        self.user_name = acct_name
        self.user_num = acct_num
        self.__user_bal = acct_balance
        # self.deposit(200)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        self.user_bal += amount
        print(f"You deposited {amount}, your new  balance is: {self.user_bal}")
    def check_balance(self):
        return self.__user_bal

tolu_acct = Account("Toluwanimi", "123456789", 0.0)
print(tolu_acct.check_balance())

# tolu_acct.user_bal = 500
# print(tolu_acct.__user_bal)
# tolu_acct.__user_bal = 500
# print(tolu_acct._Account__user_bal)
# print(tolu_acct.__user_bal)
# print(tolu_acct.user_bal)

# def welcome(user):
#     print(f"Welcpme {user}")


# welcome("vicotr")


# range(1, 6)

# inheritance

# class Father:
#     def __init__(self, first_name, last_name, age, occupation):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.occupation = occupation 
#         # print(self.introduce())

#     def introduce(self):
#         return f"Hello My name is {self.first_name} {self.last_name}, I am {self.age} years old and I work as a {self.occupation}"

# # fath_1 = Father("Olowoeko", "toluwanimi", 43, "Techprenuer")

# class Son(Father):
#     def __init__(self, first_name, last_name, age, occupation, school):
#         super().__init__(first_name, last_name, age, occupation)
#         self.school = school
#         self.salutation()
    

#     def salutation(self):
#         print(f"Hello My name is {self.first_name} {self.last_name}, I am {self.age} years old and I work as a {self.occupation}, I am attending {self.school} college")




# son_1 = Son("OBO","toluwanimi", 32, "student", school="SQI")
# son_1.introduce()
# print(son_1.school)

# multi class inheritance

# class Father:
#     def __init__(self, name, age, occupation, gender):
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#         self.gender = gender

#     def getfather_property(self):
#         print(f"this are the properties i got from my father {self.name}, {self.occupation}, {self.gender}")


#     def activate(self):
#         print("Activating....")
# father = Father("oluwatobi", "21", "trader", "male")

# class Mother:
#     def __init__(self, character, skills):
#         self.character = character
#         self.skills = skills

#     def get_mother_property(self, skills, character):
#         print(f"I got this property from my mother: {skills} and {character}")

#     def deactivate(self):
#         print("deactiavtiong....")

# mother = Mother("Anger", "cooking")

# class child(Father, Mother):
#   def __init__(self, name, age, occupation, gender):
#       super().__init__(name, age, occupation, gender)

# child1 = child("Adeoba", "15", "student", "male")
# child1.activate()
# child1.deactivate()
# child1.get_mother_property("cooking", "anger")
# # child1.getfather_property()


# application with oop
# modularisation

