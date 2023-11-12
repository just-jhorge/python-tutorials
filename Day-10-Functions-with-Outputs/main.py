print('Day 10 Functions with outputs\n\n')

# def format_name(f_name, l_name):
#     full_name = f_name.title() + ' ' + l_name.title()
#
#     return full_name
#
#
# my_name = format_name(f_name='kwadwo',l_name='sarpong')
#
# print(my_name)

# def is_leap(year_to_check):
#     if year_to_check % 4 == 0:
#         if year_to_check % 100 == 0:
#             if year_to_check % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(input_year, input_month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if month > 12 or month < 1:
#         return "Invalid month"

#     if is_leap(input_year) and month == 2:
#         return 29
#     return month_days[month - 1]


# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# days = days_in_month(input_year=2022, input_month=2)
# print(days)


def add (n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    operations = { "+": add, "-": subtract, "*": multiply, "/": divide }
    num1 = int(input('What is the first number: '))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operator = input('Pick an operation: ')
        num2 = int(input('What is the next number: '))
        operation = operations[operator]
        answer = operation(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}\n")

        restart = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        
        if restart == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

