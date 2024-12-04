############DEBUGGING#####################

# # Describe Problem

# problem : its not reach 20 and statement ' You got it' not printed
# def my_function():
#     for i in range(1, 20):
#       # print(i) 1-19
#       if i == 20:
#         print("You got it")
# my_function()

#solution
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

#problem: after running more than 6 times its produce an error.
#error: list index out of range
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# #if the dice_num reach 6 error occur
# print(dice_images[dice_num])

# #solution
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num-1])

#problem: just play computer . until you feel want to enter year 1994
#error: after input 1994 non occur
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # solution
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

#Problem: you notices red underlined below. after run there is indented block
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")

#solution
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#problem: try print every single line until you find erro
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# # print(word_per_page) error occur above whereas there is double equal .
# total_words = pages * word_per_page
# print(total_words)

#solution
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

import random
import maths
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
