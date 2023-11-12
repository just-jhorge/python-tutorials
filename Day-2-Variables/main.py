print('Welcome to the tip calculator.')

total_bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
total_persons = int(input('How many people to split the bill? '))

total_bill_plus_tip = ((tip / 100) * total_bill) + total_bill
person_payable = total_bill_plus_tip / total_persons

print(f"Each person should pay: ${round(person_payable, 2)}")