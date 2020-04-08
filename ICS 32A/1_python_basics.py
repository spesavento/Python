
# This is a comment in Python
# * Python is case - sensitive!!

# >>> is called a shell prompt
# REPL - read, evaluate, print, loop - the way Python interacts and reads the 
#        expression typed into the shell prompt

# When you press the upper right run button ">", only the outputs with print() statements
# will show up!
# press shift + return to run a single line, now you can evaluate without print() and see shell prompts

4
'Hello'

# Using operators + - * /
2 + 2
19 - 6
3.5 + 2.25
5 * 4
12 / 4

# notice that 12/4 returns 3.0 instead of 3.
# This is because / always returns the fractional part, even if it's 0

### Errors 
# Boo is sleeping next to me
# SyntaxError: invalid syntax 
# 5 / 0
# ZeroDivisionError: division by zero

### Types or Classes ()
# integers, floats, strings, 

#integers -- int 
#integers don't have a fractional part to them. There is no limit to how large or small they may be.
type(4)
type(-15)
type(0)
type(123456789012345678901234567890)

# float
# a float is a number with a fractional part. It does have a limit, although it varies.
type(4.5)
type(11.875)

# Notice that floats convert to integers
5 + 4.1
15 / 3
15.0 / 3.0
15 // 3
15.0 // 3.0
16 / 5       # always yields a non-integer
16.0 // 5.0  # returns floor division - rounds 3.2 down to a 3.0
16 // 5.0
16 // 5      # returns integer floor division
60 / 9 
60 // 9 
2.1 ** 3.3 # power
7 % 3 
9 % 3 # remainder / modulo

# why remainder? 
# you can check if numbers are even or odd by using the n %% 2 == 0 or n %% 2 == 1
# note that n %% m lies between 0 and m - 1

# PEMDAS applies to parenthesis (or lack thereof)
3 + 4 * 5
5 - 3 - 2  #evaluated left to right
4 ** 3 ** 2  #4^3^2 is actually evaluated as right-to-left as in math --> 4^6
4 ** 9


### Variables!
boo = 11
boo
boo * 4
type(boo)
# Variables in Python don't have a type! Just the value it holds does.

# variable names in Python only use lowercase letters, numbers, and underscores
# it MUST start with an underscore or lowercase letter
# uppercase letters work, but it's not the convention (and Python is case-sensitive)

# Relational operators -- logical expressions
# BOOLEAN type
# they output either True or False
3 == 3
4 == 4
3 != 3
3 < 3
4 >= 3
True == 1
False == 0
#These are not assinging a values to a variable, they are checking the relation of values
4.0 == 4.0
3 < 4.0 
# you can chain them, in which case ALL have to be true in order to make the expression true
2 < 4 < 8
2 < 4 < 3
x = 3
0 < x < 5
y = 4
z = 5
x == y == z
type(3 > 4)

True == False
True != False

# the "not" operator negates the boolean
not True

# and / or operators
True and True and False and True
True or True or False or True
a = 12
b = 9
a < 15 and b > 0 
a < 10 or b == 10 

# only name your Python files with lowercase letters, numbers, underscores

# print() will be needed to display your output after running the code
# With multiple values, print() outputs are seperated with a space, use the 
# sep="" to get rid of the space. These are called keyword arguments.

print(10,4)
print(10, 2.5)
print(10, 2.5, sep="")
print("Hello", "Sara", sep="")
print("Hello", "Sara", sep="eee")

# by default, print() ends in a new line to take in a new argument
# you can use the keyword argument of end= to change this
print("Hello", "Sara", end="xxx")  #doesn't end it on a new line but gives the prompt on the same line
print("Hello", "Sara", end="xxx\n") #\n is a new line character

x = 5
y = 7.5
z = 10
print(x, y, sep = 'q', end = '')
print(z)   #automatically adds a new line because there end defaults to that
print(x + y + z) #blank space seperation and new line 

##### Strings
#strings are a type made up of 0 or more characters
x = "Hello"
type(x)
str_str = '\'Hello my name is Sara\', she said.'  #imbedded quotes - single
str_str
str_str_double = "'Hello my name is Sara', she said." #imbedded quotes - single within double
str_str_double

#new lines = \n
print("Hello\nSara")
print('Hello\nSara')
#what if you want to see the \n? use and extra \
print("day\night")
print("day\\night")  #two \\ become a single \

# length of a string 
len('Boo')
len('a\\b')
len('too\nme') #\n is a character

# concatenation and multiplication

'abc' + 'def'
'boo' * 3

# METHODS
# The values that Python programs operate on are called objects
# Many objects in Python support methods, which are similar to functions, but
# instead you ask an object to perform on your behalf
# When you want to call a method on an object, (aka asking the object to do something for you)
# you do so by following the object with a dot, the name of the method, then the arguments surrounded by the parenthesis

description = '    Boo is happy today!   '
description.strip()
#The strip method returns the string it's called on, without any spaces at the beginning or end

description.upper()
description.isupper()

'Boo'.upper()
'Boo'.upper().isupper()

description.startswith('B')
description.startswith(' ')
description.strip().startswith('B')  #you can string methods together


#Python contains a built-in function called input() which allows the user to input a value
# The function won't finish until the user presses Enter or Return

x = input()
#notice that it inputs a string of whatever you enter --> hello becomes "hello" and 34 becomes "34"
#this is because the user can put any kind of data type and anything they they enter can be made a string!

# Type Conversions
#We can always change the data type as needed
# int() float() str() bool()
int('35')
type(int('35'))
str(35)
str('False')
float('10.5')
int('    15   ')  #strips front and end spaces
#for bool, non-empty is True and empty is False
bool('True')
bool('False')
bool('123')
bool('')

#if you want to make sure they enter an integer, you can do:
age = int(input('Enter your age: '))
age
#we can handle non-integer inputs later

### if statements
value = int(input('Enter a number: '))

#if(true)  next line MUST be indented in Python
if value > 0:
    print('That number is positive')

print('Goodbye!')

#IF ELSE

num = int(input('Enter a number: '))

if num > 0:
    print('That number is positive')
elif num < 0:
    print('That number is negative')
else:
    print('That number is zero')


### while
num = int(input('Enter a number: '))

while num > 0:
    print(num)
    num -= 1
print('Goodbye')

#a break statement can be included within the loop to leave the loop
while True:
    name = input('Enter your name: ')

    if name == '':
        print('Please enter a name; you entered nothing')
    else: break 

print('Your name is ' + name)


#### adding an else statement to a while loop
# this else statement executes when the loop ends, but only if it ends properly (not break before)
total = 0
count = 0

print('Please enter 10 non-zero numbers')

while count < 10:
    num = int(input('Next number: '))

    if num == 0:
        print('That number was zero; no sum for you!')
        break
    else:
        total += num
        count += 1
else:
    print('Thank you!  The sum of these numbers was', total)

### ranges  -- type = range
## range(start, stop, step)
#note: STOP is NOT inclusive of end number
range(1, 10, 2)
type(range(1, 10, 2))
len(range(1, 10, 2)) #1 3 5 7 9 
len(range(1, 11, 2)) #1 3 5 7 9 
#if no step specified, then it's automatically 1
range(1, 10) #(1 to 9)
len(range(1,10))
#if only one argument is passed, the start defaults to 0
range(6)
len(range(6))  #(0 to 5)

r = range(1,10)
r[0]
r[2]

#### for loop

total = 0

for num in range(1, 10):
    total += num

print('The sum is', total)

for i in range(15):
    print('Boo')

#note: like while loops, for loops in Python can have the ending else statement

for i in range(3):
    user_num = int(input('Input a number: '))

    if user_num > 50:
        print('Uh oh, greater than number. Program breaks now.')
        break
else:
    print('Congrats! You made it!')

