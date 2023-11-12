# RANDOMISATION AND PYTHON LISTS

# Randomisation

import random

# random_int = random.randint(1,10)
# random_float = random.random()
#
# love_score = random.randint(1,100)
#
# print(random_int)
# print(random_float)
# print(f"Your love score is {love_score}")

# number = random.randint(0,1)
#
# if number == 1:
#     print("Heads")
# elif number == 0:
#     print("Tails")

# print('Who is paying?')
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(', ')
#
# print(len(names))
#
# person_to_pay = names[random.randint(1, len(names) - 1)]
#
# print(f"{person_to_pay} is going to buy the meal today!")

# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears',
#                'Tomatoes', 'Celery', 'Potatoes']

# fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen)

# row1 = ['⬜', '⬜', '⬜']
# row2 = ['⬜', '⬜', '⬜']
# row3 = ['⬜', '⬜', '⬜']
# map = [row1, row2, row3]
#
# print(f"{row1}\n{row2}\n{row3}\n")
#
# position = input('Where do you want to put the treasure? ')
#
# column_number = int(position[0])
# row_number = int(position[1])
#
# selected_row = map[row_number - 1]
# selected_row[column_number - 1] = 'X'
#
# print(f"{row1}\n{row2}\n{row3}\n")


# Rock, Papper, Scissors
# Rules
# 1. Rock wins against scissors
# 2. Scissors wins against paper
# 3. Paper wins against rock

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

user_index = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
cpu_index = random.randint(0, len(options) - 1)

user_choice = options[user_index]
cpu_choice = options[cpu_index]

print(user_choice)

print('Computer chose:')

print(cpu_choice)

if user_choice == rock and cpu_choice == scissors:
    print('You win')
elif user_choice == scissors and cpu_choice == paper:
    print('You win')
elif user_choice == paper and cpu_choice == rock:
    print('You win')
elif user_choice == cpu_choice:
    print('A draw')
else:
    print('You lose')

