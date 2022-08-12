# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
'''#Task 1
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c= int(input("Enter second number:"))
sum = a+b+c 
print("The tripple sum is:"+ str(sum))'''
'''#Task2
for i in range(3):
    a =int(input("First number "))
    b = int(input("Second number "))
    if a > b:
        diff = a - b
    else:
        diff = b - a

    print("The result of the calculation is:" + str(diff))'''
'''#Task 3
for i in range (2):
    a = int(input("Enter a number: "))
    if (a % 2) == 0:
        print("{0} is Even an even number ".format(a))
    else:
        print("{0} is Odd number ".format(a))'''
'''# Task 4
import math
r = float(input("Input the radius of the circle :"))
print("The area of the circle is:"+ format(float(math.pi* r**2 ),".2f"))'''
'''#Task 5
import random
target_num , guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')'''
#Task 6
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))