# we want to find common divisor for two number
first_number  = int(input('First Number:'))
second_number = int(input('Second Number:'))


# E0: if first_number < second_number
#     --yes-> 
#            first_number <-> second_number, go to next step
#     --No->
#           go to next Step
# E1: if first_number/second_number = quotion + reminder/ second_number  
#     --yes->
# E2:        if reminder != 0 
#            --yes-> 
# E3:               first_number <- reminder , first_number <-> second_number, go to next step
#             --No-> 
#                   Terminate , go to next step

if first_number < second_number:
    tmp = first_number  
    first_number = second_number
    second_number = tmp

quotion = first_number//second_number
reminder = first_number % second_number

while first_number/second_number == quotion + reminder/ second_number:

    if reminder != 0:
        first_number = reminder

        tmp = first_number  
        first_number = second_number
        second_number = tmp
        quotion = first_number//second_number
        reminder = first_number % second_number
    else:
        break

print('common divisor:',second_number)
