# There are two types of loop:
# FOR LOOP
# WHILE LOOP

# for loop
# N.B. expression, iteration, iterate and iterable
# break, continue and pass

# while loop
# initialization, condition, code, increment


# fruits = ["berry", "orange", "banana", "melon", "cherry"]
# for i in fruits:
# # i is iterate, fruits is iterable
#     print(i)
#     if i == "melon":
#         break
#     print("close end")

# Nested loop
# for i in range(1, 13):
#     print(f"Multiplication Table {i}")
#     for x in range(1, 13):
#         print(f"{i} * {x} = {i*x}")
#         # break


# x = 1
# while x <= 10:
#     print(x)
#     x += 1


# cars = ["Toyota", "Honda", "Nissan", "BMW", "Ford", "Audi", "Porshe"]
# for x in cars:
#     print(x)
#     if x == "BMW":
#         break



# i = 0
# while i < len(cars):
#     x = cars[i]
#     print(x)
#     if x == "BMW": 
#         break
#     i += 1

tickets = 5
vip_ticket = 2
while tickets > 0:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are too young for this, go and watch cartoon")
        break
    print("Ticket available")
    print("""
        1. Regular
        2. VIP
        """)
    option = input("Which ticket do you want to buy: ")
    if option == "1":
        print("""Welcome to the Home of movies, 
        choose your preferred movie below:
            1. Avatar
            2. AOT
            3. Black clover
            4. Spiderman
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Go to room 1, for regular section")
        tickets -= 1
        print(f"selling out soon, {tickets} tickets remaining")
        continue
    elif option == "2":
        if vip_ticket < 1:
            print("No more VIP tickets available, come back tomorrow")
            continue
    print("""Welcome to the Home of movies, 
        choose your preferred movie below:
            1. Avatar
            2. AOT
            3. Black clover
            4. Spiderman

            """)
    choice = input("Enter your choice")
    if choice == "1":
        print("Go to room 4, for vip section")
        vip_ticket -= 1
    else:
        print("No more tickets available, come back tomorrow")

# i = 0
# while i > 0:
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)