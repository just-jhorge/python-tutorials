# fruits = ['Apple', 'Peach', 'Pear']
#
# for fruit in fruits:
#     print(fruit)

# student_heights = [180, 124, 165, 173, 189, 169, 146]
# student_heights = input("Input a list of student heights separated by a space: ").split()
# total_height = 0
#
#
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#
# for height in student_heights:
#     total_height += height
#
# average_height = round(total_height / len(student_heights))
# print(f"Average height for the class is: {average_height}cm")

# student_scores = input('Input a list of student scores: ').split()
#
# max_score = 0
#
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#
# print(student_scores)
#
# for score in student_scores:
#     if score > max_score:
#         max_score = score
#         print(f'{score} is the current max value.')

# total_sum = 0
#
# for n in range(1, 101):
#     if n % 2 == 0:
#         total_sum += n
#
# print(total_sum)

# for n in range(1,101):
#     if n % 3 == 0 and n % 5 == 0:
#         n = 'FizzBuzz'
#     elif n % 3 == 0:
#         n = 'Fizz'
#     elif n % 5 == 0:
#         n = 'Buzz'
#
#     print(n)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator\n')
num_of_letters = int(input('How many letters would you like: '))
num_of_symbols = int(input('How many symboles would you like: '))
num_of_numbers = int(input('How many numbers would you like: '))

password_list = []
password = ""

for char in range(0, num_of_letters + 1):
    password_list.append(random.choice(letters))

for n in range(0, num_of_numbers + 1):
    password_list.append(random.choice(numbers))

for n in range(0, num_of_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f'Your generated password is: {password}\n')

print('Thank you for using a app, do well to drop a review soon')


