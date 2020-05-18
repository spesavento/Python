#for and while loops

count = 0 
print('Starting') 
while count < 10:
    print(count, ' ', end='') # part of the while loop
    count += 1 # also part of the while loop 
print() # not part of the while loop
print('Done')

#print with \n after each iteration
for i in range(0, 10): #notice it doesn't include 10
    print(i) 
print()
print('Done')

#print one space apart
for i in range(0, 10):
    print(i, ' ') 
print()
print('Done')

#print with no spaces
for i in range(0, 10): 
    print(i, end='') 
print()
print('Done')
for i in range(3):
   print(i)


#range(0,10) increments by 1 automatically
#To increment by different intervals, use a thrid argument
print('Print out values in a range with an increment of 2') 
for i in range(0, 10, 2):
    print(i, ' ', end='') 
print()
print('Done')

for _ in range(0,10): 
    print('.', end='')
print()

#break statement to end the loop
print('Only print code if all iterations completed') 
num = int(input('Enter a number to check for: ')) 
for i in range(0, 6):
    if i == num: 
        break
    print(i, ' ', end='') 
print('Done')

#continue statement to move onto the next iteration
for i in range(0, 10): 
    print(i, ' ', end='') 
    if i % 2 == 1:
        continue
    print('hey its an even number') 
    print('we love even numbers')
print('Done')

# For loop with an else condition!
#note that the else is optional
#It is only executed if ALL the sequence items are processed
#if it's ended early i.e. syntax error or break statement, it's NOT run

# Only print code if all iterations completed over a list print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
    if i == num: 
        break
    print(i, ' ', end='') 
else:
    print()
    print('All iterations successful')

# Dice Roll Game!
import random
MIN = 1
MAX = 6
roll_again = 'y'
while roll_again == 'y': 
    print('Rolling the dices...') 
    print('The values are....') 
    dice1 = random.randint(MIN, MAX) 
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Roll the dices again? (y / n): ')

#Exercises 
#1.  Write a program that can find the factorial of any given number. 
#    For example, find the factorial of the number 5 (often written as 5!) 
#    which is 1 * 2 * 3 * 4 * 5 and equals 120.
#    The factorial is not defined for negative numbers and the 
#    factorial of Zero is 1; that is 0! = 1.

#1. If the number is less than Zero return with an error message.
#2. Check to see if the number is Zero—if it is then the answer is 1—print this out. 
#3. Otherwise use a loop to generate the result and print it out.

user_input = int(input("Enter a number: "))
if user_input <  0:
    print("The number must be greater or equal to 0.")
else:
    if user_input == 0:
        fact = 1
    else:
        fact = 1
        for i in range(1, user_input+1): #it's UP to, not including, user_input + 1
            fact *= i
    print("The factorial of", user_input, "is", fact)

#2.   Print all the prime numbers in a range
#     Prime number can only be divided by themselves and 1

user_input = int(input("Enter a number above 1: "))
if user_input <  1:
    print("The number must be above 1.")
else:
    for i in range(2, user_input+1): #go up to the user_input
        is_prime = 0 
        for j in range(2, i): #it won't be divisible by anything greater than itself. Don't include i because it's always divisible by itself.
            #range(2,2 does not iterate) so is_prime stays 0 
            if i%j == 0: #if divisible it's NOT a prime number
                is_prime = 1
                break  #break out and try the next number
        if is_prime == 0:
            print(i, ' ', end = '')
