# Python collection and arrays
# Python methods are input functions we can use to manipulate strings, lists, and other data types. They are built-in functions that allow us to perform specific operations on data. 
# String Methods

# name = "emmie"
# user_name = input("Enter your name: ")
# if name == user_name.casefold():
#     print("Welcome back, Emmie!")
# else:
#     print("Hello, stranger!")

# x = "BANANA"
# print(x.capitalize())  # Output: Banana
# print(x.casefold())  # Output: banana
# print(x.capitalize())  # Output: Banana
# print(x.center(20, "*"))  # Output: *******BANANA*******
# print(x.casefold().count("a"))  # Output: 3
# print(x.count("A"))  # Output: 3
# print(x.count("A", 0, 3))  # Output: 2
# print(x.encode())  # Output: b'BANANA'


# print(x.endswith("A"))  # Output: True
# print(x.endswith("A", 0, 3))  # Output: True

# print(x.expandtabs())  # Output: BANANA

# print(x.find("A"))  # Output: 1
# print(x.find("A", 0, 3))  # Output: 1

# print(x.format())  # Output: BANANA

# print(x.index("A"))  # Output: 1

# print(x.isalnum())  # Output: True
# print(x.isalpha())  # Output: True
# print(x.isdigit())  # Output: False
# print(x.islower())  # Output: False
# print(x.isupper())  # Output: True
# print(x.isspace())  # Output: False
# print(x.isascii())  # Output: True

# greeting = ["hello", "world"]
# print(" ".join(greeting))  # Output: hello world
# print(" ".join(["Hello", "world"]))  # Output: Hello world

# y = "Banana is a fruit"
# print(y.split())  # Output: ['Banana', 'is', 'a', 'fruit']

# z = "///apple////"
# print(z.strip("/"))  # Output: apple



# # List methods
# fruits = ["apple", "banana", "cherry", "mango"]

# print(fruits.append("orange"))  # Output: None (modifies the list in place)
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# print(fruits.count("banana"))  # Output: 1 because "banana" appears once in the list
# print(fruits.index("banana"))  # Output: 1
# print(fruits.index("grape"))  # Output: ValueError: 'grape' is not in list
# print(fruits.insert(2, "kiwi"))  # Output: None (modifies the list in place)
# print(fruits)  # Output: ['apple', 'banana', 'kiwi', 'cherry', 'mango', 'orange']
# print(fruits.pop())  # Output: 'orange' (removes and returns the last item)
# print(fruits)  # Output: ['apple', 'banana', 'kiwi', 'cherry', 'mango']
# print(fruits.remove("banana"))  # Output: None (modifies the list in place)
# print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'mango']
# print(fruits.reverse())  # Output: None (modifies the list in place)
# print(fruits)  # Output: ['mango', 'cherry', 'kiwi', 'apple']



# cars = ["toyota", "honda", "lexus", "porshe", "benz", "lambo", "bmw", "brabus"]
# price = ["12m", "7m", "20m", "30m", "25m", "40m", "30m", "70m"]
# for each_car, each_price in zip(cars, price):
#     print(f"{each_car}: {each_price}")
# result_db = []
# questions = [
#     "what is the country with the most island in the world",
#     "what is the country with the highest currency rate",
#     "what is the country with the best president",
#     "what is the country with the higest population",
# ]

# answer = [
#     "sweden",
#     "kuwait",
#     "Nigeria",
#     "india"
# ]

# while True:
#     print("""
#     Welcome to the Quiz!
#     1. take quiz
#     2. view results
#     3. exit
    
#     """)
#     Choice = input("Enter your choice: ")
#     if Choice == "1":
#         Name = input("Enter your name: ")
#         score = 0
#         for each_ques, each_ans in zip(questions, answer):
#             print(each_ques)
#             user_ans = input("Enter your answer: ")
#             if user_ans.casefold().strip(" ") == each_ans.casefold():
#                 score += 1
#                 print("Correct")
#             else:
#                 print("Olodo rabata")
#         user_details = {
#             "Name": Name,
#             "score": score
#         }
#         result_db.append(user_details)
#         print("thanks for taking the quiz")
#     elif Choice == "2":
#         each_user_res = result_db[name]
#         name = input("Enter your name: ")
#         if name.casefold().strip(" ") == each_user_res["Name"].casefold():
#             print(f"{each_user_res['Name']}: {each_user_res['score']}/{len(questions)}")
#         else:
#             print("Results not available")
            
#         pass
#     elif Choice == "3":
#         print("Exiting the quiz...")
#         break


# Tuple methods
# xteristics of tuple
# 1. tuples can be index
# 2. tuples accept duplicate values
# 3. tuples are immutable
# indexing and slicing

# fruits = ("apple", "banana", "cherry", "mango", "orange")
# print(fruits[3])
# fruits[0] = "banana"
# print(fruits)
# print(type(fruits))
# print(fruits.count("apple"))
# print(fruits.index("cherry"))


# Dictionaries methods
# xterictics
# 1. it takes keys and values
# 2. Dictionaries are mutable

# user = {
#     "name" : "Idan Emmie",
#     "password" : "12345",
#     "age" : "18",
#     "course" : "Software Engineer"
# }
# print(type(user))
# print(user[0])
# print(user["name"])
# user["name"] = "lovely emmie"
# print(user)
# print(user["age"], user["name"])
# emma = user.copy()
# print(emma)
# print(user.fromkeys(["first_name"], "ade"))
# print(user.get("age"))
# print(user.items())
# for each_user in user.items():
#     print(each_user[1])
#     print(f"{each_user[0]}: {each_user[1]}")

# for index, each in  enumerate(user.items(), start=1):
#     print(index, each)

# print(user.keys()) #it returns a list of keys
# print(user.values()) #it returns a list of values
# print(user.pop("age")) #remove age from the items
# print(user)
# print(user.clear()) #clear all items
# print(user)
# print(user.popitem()) #delete last item only
# print(user)
# print(user.setdefault("name","age"))

#Assignment 
# Have a teacher section where teachers can check for student with higest and lowest score. they can also update questions

result_db = []
cbt = {
    "what is the country with the most island in the world":"Sweden",
    "what is the country with the highest currency rate":"Kuwait",
    "what is the country with the best president":"Nigeria",
    "what is the country with the higest population":"India"
}



while True:

    print("""
    Welcome to SQI cbt exam
    1. Take test
    2. Check result
    3. Teacher section
    4. Exit
        """)

    choice = input("Enter your choice: ")
    if choice == "1":
        score = 0
        name = input("Enter your name: ")

        for index, each in enumerate(cbt.items(), start=1):
            print(f"{index}: {each[0]}")
            user_ans = input("Enter your ans: ")
            if user_ans.casefold().strip(" ") == each[1].casefold():
                print("Correct")
                score+=1
            else:
                print("Olodo")

        user_details = {
            "name": name,
            "score": score
        }
        result_db.append(user_details)
    elif choice == "2":
        print("To check your result, enter your name")
        user_name = input("Enter your name: ")
        found = False
        for each_user in result_db:
            if each_user["name"] == user_name:
                print(f"{each_user["name"]}, this is your score: {each_user["score"]}")
                found = True
        if found == False:
            print("Student not found")
    elif choice == "3":
        while True:
            print("""
            Teacher Section
            1. Check highest score
            2. Check lowest score
            3. Add questions
            4. Go back
            """)
            teacher_choice = input("Enter your choice: ")
            if teacher_choice == "1":
                if len(result_db) == 0:
                    print("No student have taken the test yet")
                else:
                    highest_student = result_db[0]
                    for student in result_db:
                        if student["score"] > highest_student["score"]:
                            highest_student = student
                    print(f"{highest_student['name']} has the highest score: {highest_student['score']}")
            elif teacher_choice == "2":
                if len(result_db) == 0:
                    print("No student have taken the test yet")
                else:
                    lowest_student = result_db[0]
                    for student in result_db:
                        if student["score"] < lowest_student["score"]:
                            lowest_student = student
                    print(f"{lowest_student['name']} has the lowest score: {lowest_student['score']}")
            elif teacher_choice == "3":
                new_question  = input("Enter new question: ")
                new_answer = input("Enter the correct answer: ")
                cbt[new_question] = new_answer
                print("Question added successfully")
            elif teacher_choice == "4":
                break
    elif choice == "4":
        break



#SET METHODS
# Xteristics of set method
#1. It is unordered
#2. Does not accept duplicate values
#3. Cannot be indexed
#4. It is not mutable
# x = {"banana", "apple", "guava", "cherry", "berry"}

# x = {1,2,3,4,5,6}
# y = {3,4,5,6}
# z = {4,2}

# x.add(9) #adds 9 to the set of x
# print(x)
# p = x.copy() #duplicates set of x
# print(p)
# print(x.difference(y)) # prints what is in X but not in y
# print(y.difference(x))

# x.difference_update(y) # make more reserach on it
# print(x)

# x.discard(2) #this removes 2 form the set of x
# print(x)
# print(x.intersection(y)) # prints what is common in both x and y
# print(x.intersection_update(y)) # prints what is common in both x and y and update x
# print(x.isdisjoint(y)) # 
# print(z.issubset(x))
# print(x.issuperset(z))
# x.remove(8)
# print(x)
# print(x.symmetric_difference(y))
# print(x.symmetric_difference_update(y))
# print(x.union(y))
# x.update(y)
# print(x)
# x.clear()
# print(x)
# print(x.pop())
# print(x)





#Introductions to function
# Read on these 
# 1. Parameters
# 2. Arguments
# 3. Paramaetised and unparametised functions
# 4. Positional and keyward argument
# 5. *args and **kwargs