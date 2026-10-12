# Introduction to the JSON (JavaScript Object Notation) module in Python 

# Javascript Object Notation (JSON) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. Python provides a built-in module called `json` that allows you to work with JSON data.
# JSON is commonly used for transmitting data between a server and a web application, as well as for configuration files and data storage.
# JSON is a lists of dictioneries, where each dictionary represents a key-value pair. The keys are strings, and the values can be strings, numbers, arrays, booleans, or null.

# Dump is use to push data into a JSON string. It takes a Python object and converts it into a JSON formatted string. The `json.dumps()` function is used for this purpose.
# Dumps is used to convert a Python object into a JSON string. It takes a Python object and returns a JSON formatted string. The `json.dumps()` function is used for this purpose.
#loads is use to pull data from a JSON string. It takes a JSON formatted string and converts it into a Python object. The `json.loads()` function is used for this purpose.

# import json
# data = [{
#     "name": "Emmie",
#     "age": 25,
#     "city": "New York"
# }]

# with open("database.json", "w") as file:
#     file.write("Emmie is here")

# with open("data.json", "w") as file:
#     json.dump([{"name" : "Emmie"}, {"age": 25}, {"city": "New York"}], file, indent=4)


# # loading the json
# with open("data.json", "r") as file:
#     data = json.load(file)
#     print(data)


# with open("data.json", "w") as file:
#     json.dump(data, file)

# Recursion is a way by which a function calls itself. It is a programming technique that allows a function to solve a problem by breaking it down into smaller subproblems of the same type. Recursion is often used to solve problems that can be defined in terms of smaller instances of the same problem.



import os
import json
import datetime as dt
import pyttsx3

#Python decorators are a powerful and flexible way to modify the behavior of functions or classes. They allow you to wrap a function or class with another function, which can add functionality, modify input/output, or perform other tasks before or after the original function is called. Decorators are often used for logging, authentication, caching, and other cross-cutting concerns.
def getdatabase():
    if os.path.exists("task_db.json"):
        with open("task_db.json", "r") as file:
            return json.load(file)
    else:
        db = {
            "users": [],
            "tasks": []
        }
        with open("task_db.json", "w") as file:
            json.dump(db, file, indent=4)
        return db
#getdatabase()

def save_db(user_details):
    with open("task_db.json", "w") as file:
        json.dump(user_details, file, indent=4)

def create_account():
    db = getdatabase()
    print("Welcome, register your account!")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ").strip().casefold()
    password = input("Enter your password: ").strip()
    confirm_password = input("Confirm your password: ").strip()

    for user in db["users"]:
        if user["email"] == email:
            print("An account with this email already exists. Please try again.")
            create_account()
            return

    user_details = {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }
    tasks_details = {
        "email": email,
        "tasks": []
    }
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        create_account()
        return
    db["users"].append(user_details)
    db["tasks"].append(tasks_details)
    save_db(db)
    print("Account created successfully!")
# create_account()

def login_account():
    db = getdatabase()
    print("Welcome, please log in to your account!")
    email = input("Enter your email: ").strip().casefold()
    password = input("Enter your password: ").strip()

    for user in db["users"]:
        if user["email"] == email and user["password"] == password:
            print(f"Login successful! Welcome back, {user['name']}!")
            Dashboard(email)
            return
    print("Invalid email or password. Please try again.")

def add_task(email):
    db = getdatabase()
    for user_task in db["tasks"]:
        if user_task["email"] == email:
            task = input("Enter the task you want to add: ")
            user_task["tasks"].append(task)
            save_db(db)
            print("Task added successfully!")
            return
    print("Email not found. Please try again.")

def view_tasks(email):
    db = getdatabase()
    for user_task in db["tasks"]:
        if user_task["email"] == email:
            if user_task["tasks"]:
                print("Your tasks:")
                for idx, task in enumerate(user_task["tasks"], start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks found.")
            return
    print("Email not found. Please try again.")

def edit_task(email):
    db = getdatabase()
    for user_task in db["tasks"]:
        if user_task["email"] == email:
            if user_task["tasks"]:
                print("Your tasks:")
                for idx, task in enumerate(user_task["tasks"], start=1):
                    print(f"{idx}. {task}")
                task_number = int(input("Enter the task number you want to edit: "))
                if 1 <= task_number <= len(user_task["tasks"]):
                    new_task = input("Enter the new task: ")
                    user_task["tasks"][task_number - 1] = new_task
                    save_db(db)
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks found.")
            return
    print("Email not found. Please try again.")


def Dashboard(email):

    while True:
        print("""
        Welcome to the Dashboard!
        1. Add Task
        2. View Tasks
        3. Edit Task
        4. Delete Task
        5. Logout
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(email)
        elif choice == "2":
            view_tasks(email)
        elif choice == "3":
            edit_task(email)
        elif choice == "4":
            print("Delete task is coming soon.")
        elif choice == "5":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("""
        1. Create Account
        2. Login Account    
        3. Exit
            """)
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login_account()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

main_menu()

# Add the ability to add tasks, view tasks, and edit tasks to the dashboard.

