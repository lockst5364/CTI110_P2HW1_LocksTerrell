# P2HW1 - Calculating travel expenses
# October 19, 2023
# CTI-110 P2HW1 - Travel
# Terrell Locks
#

#expenses are entered using float strings

print('This program calculates and displays travel expenses: ')

user_budg = float(input('\nEnter budget: '))

user_dest = (input('\nEnter your travel destination: '))

user_gas = float(input('\nHow much do you think you will spend on gas? '))

user_accm = float(input('\nApproximately, how much will you need for accommodation/hotel? '))

user_food = float(input('\nLast, how much do you need for food? '))

#expenses are calculated with decimals, and aligned 

print('\n------------Travel Expenses------------')
print(f'Location:           {user_dest}')
print(f'Initial budget:     ${user_budg}')
print(f'Fuel:               ${user_gas}')
print(f'Accomodation:       ${user_accm}')
print(f'Food:               ${user_food}')
print('----------------------------------------')
remaining_bal = user_budg - user_gas - user_accm - user_food
print(f'\nRemaining Balance:  ${remaining_bal:.1f}')

#Remaining balance is displayed using float point output
