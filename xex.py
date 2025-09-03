#--------Membership Operators in Python--------#
from sys import modules

# word = "Apple"
# letter = input("Enter the letter you want to check: ")
# #  Using 'in' operator
# # if letter in word:
# #     print(f"Letter was in {letter}")
# # else:
# #     print(f"Letter was not in {letter}")
#
# #  Using 'not in' operator
# if letter not in word:
#     print(f"Letter was not found in {letter} ")
# else:
#     print(f"letter was found in {letter}")

#---------list comprehension in python-------#
# doubles = []
# for i in range(1, 15):
#     doubles.append(i-1)

# print(doubles)
# doubles=[i**2 for i in range(1, 20)]
# print(doubles)

# fruits = ['apple', 'banana', 'orange']
# fruit_char =[fruit[0] for fruit in fruits]
# print(fruit_char)

# numbers = [-2, -1, 0, 1, 2]
# negatives_num =[num for num in numbers if num < 0]
# print(negatives_num)

#--------------Match case (switch case) in python-------------#
# def day_of_week(day):
#
#         match day:
#
#             case 1:
#                 return "Monday"
#             case 2:
#                 return "Tuesday"
#             case 3:
#                 return "Wednesday"
#             case 4:
#                 return "Thursday"
#             case 5:
#                 return "Friday"
#             case 6:
#                 return "Saturday"
#             case 7:
#                 return "Sunday"
#             case _:
#                 return "Invalid day"
# day = int(input("enter the day number week (1-7):"))
# print(day_of_week(day))

# def weekend(day):
#     match day :
#         case "sunday" | "saturday" | "friday" :
#             return True
#         case "Monday" | "tuesday" | "wednesday" | "thursday":
#             return False
#         case _:
#             return"Invalid day for u man "
# print(weekend("Monday"))

#---------------Module in python----------------#

# def func1():
#     a = 10
#     return a
# def func2():
#     b = 20
#     return b
#
# x = func1() + func2()
# print(x)