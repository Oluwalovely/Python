# PYTHON COLLECTIONS AND ARRAY
# Strings


# task_db = []
# while True:
#     print("""Welcome to the Task Manager!
#     You can use the following commands:
#     1. Add a task
#     2. View all tasks
#     3. Edit a task
#     4. Delete a task
#     5. Exit
#         """)
#     choice = input("Enter your choice (1-5): ")
#     if choice == '1':
#         task_name = input("Enter the task name: ")
#         task_start_date = input("Enter the task start date (YYYY-MM-DD): ")
#         task_deadline = input("Enter the task deadline (YYYY-MM-DD): ")
#         task_description = input("Enter the task description: ")
#         save_task = {
#             'name': task_name,
#             'start_date': task_start_date,
#             'deadline': task_deadline,
#             'description': task_description
#         }
#         task_db.append(save_task)
#         harmony = task_db[0]
#         print(f"""Task added successfully!
#             Task Name: {harmony['name']}
#             Start Date: {harmony['start_date']}
#             Deadline: {harmony['deadline']}
#             Description: {harmony['description']}
#                 """)
#     elif choice == '2':
#         harmony = task_db[0]
#         print(f"""Here are all the tasks:
#             Task Name: {harmony['name']}
#             Start Date: {harmony['start_date']}
#             Deadline: {harmony['deadline']}
#             Description: {harmony['description']}
#                 """)
#     elif choice == '3':
#         task_number = int(input("Enter task number to edit: "))

#         task = task_db[task_number - 1]
 
#         task['name'] = input("Enter new task name: ")
#         task['start_date'] = input("Enter new start date: ")
#         task['deadline'] = input("Enter new deadline: ")
#         task['description'] = input("Enter new description: ")

#         print("Task updated successfully!")

#     elif choice == "5":
#         print("Exiting the Task Manager. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.") 