# user = input('Would you like to continue?')
# if user.upper !='Y' or 'YES':
#     print('Exiting')
# else:
#     print('Continuing')
#     print('Complete')

value = input('Would you like to continue? ')

if value == 'y' or value == 'yes':
    print('Continuing ...')
    print('Complete!')
elif value == 'n' or value == 'no':
    print('Exiting')
else:
    print('Please try again and respond with yes or no.')