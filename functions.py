#positional-only and keyword-only arguments
# def welcome_user(greet, name):
#     return f"{greet}, {name}, you are welcome!"
#     print(f"{greet}, {name}, you are welcome!")
# welcome_user(greet="Hello", name="John")

# #positional-only Arguments
# def welcome_user(greet, name, /):
#     return f"{greet}, {name}, you are welcome!"
# print(welcome_user("Hello", "John"))

# #keyword-only Arguments
# def welcome_user(*, greet, name):
#     return f"{greet}, {name}, you are welcome!"
# print(welcome_user(greet="Hello", name="John"))

# # *args and **kwargs
# #args means arbitrary arguments
# def create_account(*user):
#     print


# def max_score(*scores):
#     return max(scores)
# scores = [85, 90, 78, 92, 88, 100]
# print(max_score(*scores)) 


# def max_score(scores):
#     max_score = scores[0]
#     for num in scores:
#         if num > max_score:
#             max_score = num
#     return max_score
# scores = [85, 90, 78, 92, 88, 106]
# print(max_score(scores))


