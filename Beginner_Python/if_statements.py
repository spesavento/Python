3 == 5
3 != 5 
3 < 5
3 > 5
3 <=5 
3 >= 5 
#and, or, not
(3 < 4) and (5 > 4) #both conditions True
(3 < 4) or (3 > 5) #at least one condition True
not 3 < 2  #True, returns True if value is False 

num = int(input('Enter a number: ')) 

if num < 0:
    print(num, 'is negative')
elif num > 100:
    print("It's greater than 100")
else: 
    print("It's between 0 and 100")

#Nesting if statements
snowing = True
temp = -1
if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
    print('Time for hot chocolate')
print('Bye')

age = 15
status = None  #determine the status later using if statements
if (age > 12) and age < 20:
    status = 'teenager' 
else:
    status = 'not teenager'
print(status)

#Shortened -- one line assignment 
status = ('teenager' if age > 12 and age < 20 else 'not teenager') 
print(status)

#note: 0, empty strings and None equate to False
test_0 = 0 
if test_0:
    print("It equated to True")
else:
    print("It equated to False!")
if test_0 == 0: 
    print("It equated to True")
else:
    print("It equated to False!")

#Exercises 
#1. Test if an integer is positive or negative.
#   Prompt the user to input a number (use the input() function). You can assume that the input will be some sort of number.
#   Convert the string into an integer using the int() function.
#   Now check whether the integer is a positive number or a negative number.
#   You could also add a test to see if the number is Zero.

my_number = int(input("Please enter a number: "))
if my_number > 0:
    print("The number is positive!")
elif my_number < 0:
    print("The number is negative!")
else:
    print("You entered 0!")

#now let's shorten it
my_number = int(input("Please enter a number: "))
num_type = ('Positive' if my_number > 0 else 'Negative' if my_number < 0 else "Zero")
print(num_type)

#2. Test if a number is odd or even
user_num = int(input("Please enter an integer: "))
if (user_num % 2) == 0:
    print("Your number is even")
else: 
    print("Your number is odd")

#now let's shorten it
user_num = int(input("Please enter an integer: "))
print("Even" if (user_num % 2) == 0 else "Odd")

#3. Kilometres to Miles Converter
#  Make sure user entered a positive number
#  Verify that the input is a number; if it is not a number then do nothing; 
#  otherwise convert the distance to miles

try:
    my_kilometers = int(input("Please enter a number: "))
except ValueError:
    print("That's not an integer!")

if my_kilometers >= 0: #verify it's a positive numeric string
    my_kilometers = int(my_kilometers) #convert to integer
    my_miles = my_kilometers / 0.6214 #convert
    print('The miles conversion is:', round(my_miles, 2), 'miles.') 
else:
    print("Try again. Please enter a positive number.")