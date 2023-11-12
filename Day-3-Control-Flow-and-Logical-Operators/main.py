# Control flow and logical operators

# height = float(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print('You can ride the roller coaster')
#     age = int(input("How old are you? "))
#
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif 45 <= age <= 55:
#         bill = 0
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $7")
#
#     wants_photo = input('Do you want a photo taken? Y or N: ')
#
#     if wants_photo == 'Y' or 'y':
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you cannot ride the roller coaster")


# EVEN ODD QUIZ

# number = int(input('Which number do you want to check? '))

# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


# # BMI QUIZ

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
#
# bmi = round(weight / height ** 2)
#
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your bmu is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"Your bmu is {bmi}, you are overweight")
# elif bmi < 35:
#     print(f"Your bmu is {bmi}, you are obese")
# else:
#     print(f"Your bmu is {bmi}, you are clinically obese")

# # LEAP YEAR QUIZ
#
# year = int(input('Which year do you want to check? '))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not a leap year')
#     else:
#         print('Leap year')
# else:
#     print('Not a leap year')

# PIZZA ORDER

# bill = 0
#
# print('Welcome to Python Pizza Deliveries!\n')
# size = input('What size pizza do you want? S, M or L: ')
# add_pepperoni = input('Do you want pepperoni? Y or N: ')
# extra_cheese = input('Do you want extra cheese? Y or N: ')
#
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == 'Y':
#     bill += 1
#
# print(f'Your final bill is: ${bill}')

# LOVE CALCULATOR

# print('Welcome to the love calculator\n')
#
# word1 = 'true'
# word2 = 'love'
#
# name1 = input('What is your name? ').lower()
# name2 = input('What is their name? ').lower()
#
# combined_names = name1 + name2
#
# t = combined_names.count('t')
# r = combined_names.count('r')
# u = combined_names.count('u')
# e = combined_names.count('e')
#
# true = t + r + u + e
#
# l = combined_names.count('l')
# o = combined_names.count('o')
# v = combined_names.count('v')
# e = combined_names.count('e')
#
# love = l + o + v + e
#
# print(f"T occurs {t} times\nR occurs {r} times\nU occurs {u} times\nE occurs {e} times\nTotal = {true}\n")
# print(f"L occurs {l} times\nO occurs {o} times\nV occurs {v} times\nE occurs {e} times\nTotal = {love}\n")
#
# love_score = int(str(true) + str(love))
#
# if love_score < 10 or love_score > 90:
#     print(f'Your score is {love_score}, you go together like coke and mentos.')
# elif 40 < love_score < 50:
#     print(f'Your score is {love_score}, you are alright together')
# else:
#     print(f'Your score is {love_score}')


# TREASURE ISLAND
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to the Treasure Island. Your mission if to find the treasure.\n')
choice1 = input("You are at a crossroad, where do you want to go? Type 'left' or 'right': ").lower()
print(choice1)


