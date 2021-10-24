"""
Convert Minutes to Decimal
"""

# 2021/03/26
# Version 0.0.01
# Richard J Bush

vTime = float(input("Enter the time to convert to decimal "))

vHours = float((vTime//1))  # Get the Hours
vMinutes = float((vTime % 1))  # Get the Minutes


print(round(vHours, 2))  # Display Hours
print(round(vMinutes, 2))  # Display Minutes

vDecimalTime = (vHours)+((vMinutes/60)*100)  # Calculate the Time to Decimal

print(round(vDecimalTime, 2))  # Display Result & Round to 2DP
