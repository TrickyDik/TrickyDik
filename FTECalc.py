# FTE Calculator
# 2021/07/15 R.Bush

# Get Hours and Weeks
conhours = float(input('Enter Contractual Hours:'))
ftehours = float(input('Enter FTE Hours:'))
conweeks = float(input('Enter Contractual Weeks:'))
fteweeks = float(input('Enter FTE Weeks:'))

# Calculate the Hours
if conhours <= ftehours:
    hours = float(conhours / ftehours)
else:
    hours = float(1)

# Calculate the Weeks
if conweeks <= fteweeks:
    weeks = float(conweeks / fteweeks)
else:
    weeks = float(1)

# Calculate the FTE = (ConHours/FTEHours)*(ConWeeks/FTEWeeks)
FTE = float(hours * weeks)

# Print the FTE result
print('FTE is', str(FTE))
