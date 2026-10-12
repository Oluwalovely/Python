#ERROR HANDLING
# We have 4 different types of block TRY BLOCK, EXCEPT BLOCK, ELSE BLOCK, FINALLY BLOCK

#TRY BLOCK
#

#EXCEPT BLOCK
#This is the block where the error message lies in. It is the code that runs when the TRY block refuse to run.

# ELSE Block
# This contains the result of th try block. This what the backend returns to the frontend.

#FINALLY BLOCK
#This is the block that runs whether there is an error or not.

#There are different types of error:
# 1. The compile time error: these are the error that occurs at the process of compiling your code
# 2. Run time error: These errors are only detected at the process of running your code e.g value error, key error, attibute error, zero division error, name error, type error, index error, time-out error, module not found error

#SQL ERROR
# Integrity error: it has to do with duplicate values

# try:
#     x = int(input("Enter your number: "))
# except ValueError as e:
#     print("input field must be a numeber")
# else:
#     print(x)
# finally:
#     print("Goodbye")


# user = {
#     "name" : "Emmie Baba",
#     "age": "20",
#     "email": "emmiebabs@gmail.com"
# }

# try:
#     print(user["phone_number"])
# except Exception as e:
#     print("key not found", e)
# else:
#     print("ket is found")

# try:
#     x = (1,2,3,4,5)
#     print(x[9])
# except Exception as e:
#     print("error", e)