# we want to find common divisor for two number

from tokenize import Number


first_number  = int(input('First Number:'))
second_number = int(input('Second Number:'))

is_not_common = True
quotion = first_number//second_number
reminder = first_number % second_number
print(quotion)
print(first_number//second_number)
print('reminder:',reminder)
while first_number/second_number == quotion + reminder/ second_number:
    if first_number < second_number:
        tmp = first_number  
        first_number = second_number
        second_number = tmp

    reminder = first_number % second_number
    if reminder != 0:
        first_number = reminder
        quotion = reminder
    else:
        is_not_common = False

print('common divisor:',quotion)
