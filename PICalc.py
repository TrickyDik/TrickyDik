# Pensions Increase Calculator

print('Enter the Basic Pension')
basicPension = float(input())  # Ask user for the current Basic Pension

if basicPension <= 0:
    print('Basic Pension is zero - no increase')


print('Enter the Basic Pension Increase')
basicPI = float(input())  # Ask the user for the current Basic PI

print('Enter the new PI rate %')
newPIRate = float(input())  # Ask the user for the new percentage rate for PI

newPI = round((basicPension+basicPI)*newPIRate -
              basicPension, 2)  # Calculate the new PI due

print('New Basic Pension Increase due')
print(newPI)  # Output
