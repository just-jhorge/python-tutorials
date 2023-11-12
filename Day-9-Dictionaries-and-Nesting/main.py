# programming_dictionary = {
#     'Bug': 'An error in a program that prrevents the program from running as expected',
#     'Function': 'A piece of code that you can call over and over again',
#     'Loop': 'An action of doing something over and over again',
# }
#
# # Retrieving an item from a dictionary
# # print(programming_dictionary['Bug'])
#
# # Adding an item to a dictionary
# programming_dictionary['Argument'] = 'Data that is provided to a function while it is being called.'
#
# # Create an empty dictionary
# empty_dictionary = {}
#
# # Wiping an existing dictionary
# # programming_dictionary = {}
#
# # Editing an item in a dictionary
# programming_dictionary['Bug'] = 'An insect in code.'
#
# # Looping a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# # print(programming_dictionary)

# student_scores = {
#     'Harry': 81,
#     'Ron': 78,
#     'Hermoine': 99,
#     'Draco': 74,
#     'Neville': 62
# }
#
# student_grades = {}
#
# grade_text = ''
#
# for key in student_scores:
#     score = student_scores[key]
#
#     if 91 <= score <= 100:
#         grade_text = 'Outstanding'
#     elif 81 <= score <= 90:
#         grade_text = 'Exceeding expectation'
#     elif 71 <= score <= 80:
#         grade_text = 'Acceptable'
#     else:
#         grade_text = 'Fail'
#
#     student_grades[key] = grade_text
#
# print(student_grades)

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ['Paris', 'Lille', 'Dijon'],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'],
#         "total_visits": 5
#     }
# ]
#
#
# def add_new_country(country, times_visited, cities_visited):
#     travel_log.append({
#         "country": country,
#         "times_visited": times_visited,
#         "cities_visited": cities_visited
#     })
#
#
# country = input('What country did you visit? ')
# num_of_visits = int(input('How many times did you visit? '))
# cities = input('Which cities did you visit? Separate them with spaces: ').split()
#
# add_new_country(country=country, times_visited=num_of_visits, cities_visited=cities)
#
# print(travel_log)

print('Welcome to secret auction program')

bidders_dictionary = {}


def find_highest_bidder(bid_record):
    highest_bid = 0

    for bid in bid_record:
        bidding_amount = bid_record[bid]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bid

    print(f"The winner of the bidding is {winner} with ${highest_bid}")


should_ask_again = True

while should_ask_again:
    name = input('What is your name? ')
    bid_amount = float(input('How much do you want to bid? $'))

    bidders_dictionary[name] = bid_amount

    restart = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if restart == 'no':
        should_ask_again = False
        find_highest_bidder(bidders_dictionary)
