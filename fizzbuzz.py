"""
FizzBuzz:
if the number is divisible by 5 and 3 print FizzBuzz
else if the number is divisible by 3 print Fizz
else if the number is divisible by 5 print Buzz
"""

for i in range (1,100):
    if (i % 15) == 0:
        print('FizzBuzz')
    elif (i % 3) == 0:
        print('Fizz')
    elif (i % 5) == 0:
        print('Buzz')
    else:
        print(i)
