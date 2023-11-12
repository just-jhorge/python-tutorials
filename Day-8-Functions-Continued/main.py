# def greeting():
#     print('Hello World')
#     print('How are you all doing')
#     print('I am learning Python\n')
#
#
# greeting()
#
#
# def greet_with_name(person_name):
#     print(f'Hello {person_name}')
#     print('How are you')
#     print('Have a very good day\n')
#
#
# greet_with_name('George')
#
#
# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f"What is the weather like in {location}")
#
#
# # Positional arguments
# greet_with('Kwadwo', 'Kumasi')
#
# # Keyword arguments
# greet_with(location='Accra', name='Abena')
import math

#
# def paint_calc(height, width, coverage):
#     number_of_cans = math.ceil((height * width) / coverage)
#     print(f"You'll need {number_of_cans} cans of paint.")
#
#
# test_h = int(input('Height of wall: '))
# test_w = int(input('Width of wall: '))
# test_coverage = 5
#
# paint_calc(height=test_h, width=test_w, coverage=test_coverage)


# def prime_checker(number):
#     is_prime = True
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#
#     if is_prime:
#         print('It is a prime number.')
#     else:
#         print("It is not a prime")
#
#
# n = int(input('Check this number: '))
# prime_checker(number=n)

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(plain_text, shift_number, cipher_direction):
    message = ""

    if cipher_direction == 'decode':
        shift_number *= -1

    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            message += alphabet[new_position]
        else:
            message += char

    print(f"The {cipher_direction}d message is: {message}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(plain_text=text, shift_number=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if result == 'no':
        should_continue = False
        print('Goodbye 👋🏾')
