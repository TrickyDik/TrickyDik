from datetime import datetime

print("today's date: " + str(datetime.now()))

print("breakfast calories?")
breakfast = int(input())

print("lunch calories?")
lunch = int(input())

print("dinner calories?")
dinner = int(input())

print("snack calories?")
snack = int(input())

total = breakfast+lunch+dinner+snack
print("calorie content: "+str(total))

print('good bye')
