#20211001 2254
#version 0.0.1
#Richard J Bush

#Pay Gap Calculator

releventPay = float(input("Enter the relevent pay: "))
hoursWorked = float(input("Enter the hours worked: "))
daysInPeriod = float(input("Enter the days in period 30.44 per month or 7 per week: "))

payGapRate = round(releventPay/daysInPeriod*7/hoursWorked,2)

print(payGapRate)
