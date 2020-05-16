#Textbook - 2019_A Beginner's Guide to Python

#3 types of numbers: integers, floating point numbers, complex numbers 
#integers take up less memory
#floating point -- no fixed number of digits before or after the decimal (so it can float around)
#complex numbers are the sum of the real and imaginary part (e.g. 3 + 1j). Notice j is used instead of i

### Integers
x = 1
print(x)
print(type(x))

#convert a string (containing an integer) to an integer
int('100') #int('1.2') would give an error
int(1.0)

#Note that input() function always returns a string. 
age = int(input('Please enter your age: '))
print(type(age))
print(age)

### Floats
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

int_value = 1
string_value = '1.5'
float_value = float(int_value)
float_value = float(string_value)

exchange_rate = float(input('Please enter the exchange rate: '))
exchange_rate

### Complex Numbers
c1 = 1j
c2 = 2j
print('c1:', c1, ', c2:', c2) 
print(type(c1)) 
print(c1.real) # 0.0 (.real) + 1.0j
print(c1.imag) # 0.0 + 1.0j (.imag) 

### Boolean Values - True/False
all_ok = True 
print(all_ok) 
all_ok = False 
print(all_ok) 
print(type(all_ok))

print(int(True))  #True is 1
print(int(False)) #False is 0
print(bool(1))
print(bool(0))

### Arithmetic Operators
3 + 4
3 - 4
3 * 4
3/4 
3 // 4  #Integer division - floors the 3/4 i.e. .75 --> 0
4 % 3   #Modulus/Remainder when 4 is divided by 3
2 ** 3  #Power 2^3

# +, *, - for integers always produce an integer
home = 10
away = 15
print(home + away) 
print(type(home + away))
print(10 * 4) 
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against) 
print(type(goals_for - goals_against))

# / returns a float (always) and // returns an integer
print(100 / 20) #5.0 is a float
res1 = 3/2 #1.5
print(res1)
print(type(res1))
res1 = 3//2 #1 - floored from 1.5 integer division

4 % 2 
3 % 2 

5 ** 3  #5^3

# negatives in division
print('True division 3/2:', 3 / 2) 
print('True division 3//2:', -3 / 2) 
print('Integer division 3//2:', 3 // 2) 
print('Integer division 3//2:', -3 // 2) #notice -1.5 is floored to -2 (always rounded down toward -inf)

### Floating Point Operators
print(2.3 + 1.5) #3.8
print(1.5 / 2.3) #0.6521739130434783
print(round(1.5 / 2.3, 2)) #0.65
print(1.5 * 2.3) #Notice instead of 3.45 it's 3.4499999999999997
print(2.3 - 1.5) #Notice instead of .8 it's 0.7999999999999998
i = 3 * 0.1  #integer and float = float
print(i)  #0.30000000000000004
#Why is it not .3? floating point (or real) numbers are represented as an approximation 
#There are libraries in Python to handle this e.g. decimal
from decimal import getcontext, Decimal
#set the precision 
getcontext().prec = 2
output = 3 * Decimal(.1)
output #Decimal('0.30')
type(output) #<class 'decimal.Decimal'>
float(output)  #0.3

### Assignment Operators

#compound operators
x = 0 
x += 5 #same as x = x + 5  --> 5
x -= 1 #same as x = x - 1  --> 4
x *= 1 # 4
x /= 4 # 1.0
x //= 1 # still 1.0 because float/int
x = 10
x %= 4  # 2
x **= 3 # 8

### None

# None is the non-value in Python of the NoneType

winner = None
print('winner:', winner) #winner: None
print('winner is None:', winner is None)  #True
print('winner is not None:', winner is not None) #False
print(type(winner)) #<class 'NoneType'>

#Exercises 
#Write a program to convert a distance in Kilometres into a distance in miles.
#   1. Take input from the user for a given distance in Kilometres. 
#      This can be done using the input() function.
#   2. Convert the value returned by the input() function from a string into an 
#      integer using the int() function.
#   3. Now convert this value into miles—this can be done by dividing the 
#      kilometres by 0.6214
#   4. Print out a message telling the user what the kilometres are in miles.

my_kilometers = int(input('Input kilometers for conversion: '))
my_kilometers #should be an integer
my_miles = my_kilometers / 0.6214
print('The miles conversion is:', round(my_miles, 2), 'miles.') 
#Notice: the print function automatically seperates by a space where there is a comma!










